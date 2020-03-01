# -*- coding: utf-8 -*-

"""
==============
Second Hand Ad
==============

Base class for all the specific ad items.
"""

from __future__ import division, print_function, absolute_import

from datetime import datetime, timedelta
from geopy.geocoders import Nominatim
from urllib.parse import urljoin

from scrapy import Field, Item
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity, Join, MapCompose, TakeFirst

from homespace._wrangling import extract_price_value, format_datetime, format_text, remove_all_spacing, serialize_html_tag

#####################################################################
# SERIALIZE DATETIMES
#####################################################################

def parse_datetime(
        text: str,
        loader_context: dict) -> str:
    """
    Format the dates according to ISO 8601.

    The loader context is setup by the crawler to match the formating
    of its target website.

    Parameters
    ----------
    text: str.
        The serialized datetime, as displayed on the website.
    loader_context: dict.
        The item load context.

    Results
    -------
    out: str.
        The serialized datetime, in ISO 8601 format.
    """
    return format_datetime(
        string=text,
        format=loader_context.get('datetime_format', '%Y-%m-%dT%H:%M:%S'))

#####################################################################
# GENERIC AD
#####################################################################

class SecondHandAd(Item):
    """
    The data of each ad is stored in an 'item' object, waiting for
    further processing.

    The generic item is composed of:
    - ad information
    - vendor information
    - item information
    """
    # Ad
    url = Field()
    vendor = Field()
    title = Field()
    price = Field()
    condition = Field()
    location = Field()
    first_posted = Field()
    last_updated = Field()
    description = Field()
    images = Field()

    # Generic
    brand = Field()
    model = Field()
    make = Field()
    color = Field()
    price_new = Field()

    # Additional
    latitude = Field()
    longitude = Field()
    age = Field() # in days
    user_rating = Field()

    # Evaluation & sorting
    value_rating = Field()
    leverage_rating = Field()

    # Dataviz
    icon = Field() # for map markers
    summary = Field() # all the information as an html paragraph

class SecondHandAdLoader(ItemLoader):
    """
    Generic ad loader: cleans and formats the raw data scraped from
    the webservices.

    The data of each ad is then stored in an 'item' object, waiting for
    further processing.
    """

    default_output_processor = TakeFirst()

    url_in = MapCompose(format_text)
    url_out = Join()

    vendor_in = MapCompose(format_text)
    vendor_out = Join()

    title_in = MapCompose(format_text)
    title_out = Join()

    price_in = MapCompose(format_text, remove_all_spacing, extract_price_value)
    price_out = TakeFirst()

    condition_in = MapCompose(format_text)
    condition_out = Join()

    location_in = MapCompose(format_text)
    location_out = Join()

    first_posted_in = MapCompose(format_text, parse_datetime)
    first_posted_out = Join()

    last_updated_in = MapCompose(format_text, parse_datetime)
    last_updated_out = Join()

    description_in = MapCompose(format_text)
    description_out = Join()

    images_in = MapCompose(format_text)
    images_out = Join(', ')

    brand_in = MapCompose(format_text)
    brand_out = Join()

    model_in = MapCompose(format_text)
    model_out = Join()

    make_in = MapCompose(format_text)
    make_out = Join()

    color_in = MapCompose(format_text)
    color_out = Join()

    price_new_in = MapCompose(format_text)
    price_new_out = Join()

    user_rating_in = MapCompose(format_text)
    user_rating_out = Join()

    value_rating_in = MapCompose(format_text)
    value_rating_out = Join()

    leverage_rating_in = MapCompose(format_text)
    leverage_rating_out = Join()

    def load_item(
            self):
        """
        Complete the raw information with computed data.
        """
        __item = super(SecondHandAdLoader, self).load_item()
        __geolocator = Nominatim(user_agent='homespace')
        __location = __geolocator.geocode(
            __item.get('location', 'north pole'),
            exactly_one=True)

        # gps coordinates
        __item['latitude'] = __location.latitude
        __item['longitude'] = __location.longitude

        # timeline
        __item['first_posted'] = __item.get('last_updated', '')
        __item['age'] = (
            datetime.now()
            - datetime.strptime(
                __item.get(
                    'last_updated',
                    datetime.now().isoformat(sep='T', timespec='seconds')),
                '%Y-%m-%dT%H:%M:%S')).days

        # vendor
        __item['vendor'] = urljoin(
            self.context.get('base_url', ''),
            __item.get('vendor', ''))

        # evaluation & sorting depend on the query
        __item['value_rating'] = 5 # neutral value
        __item['leverage_rating'] = 5 # neutral value

        # map marker
        __item['icon'] = self.context.get('icon', 'marker')

        # summary
        __item['summary'] = (
            '{}: {} {}<br />'.format(
                'price',
                serialize_html_tag('<i>', str(__item.get('price', ''))),
                '€')
            + '{}: {} {}<br />'.format(
                'condition',
                serialize_html_tag('<i>', str(__item.get('condition', ''))),
                '')
            + '{}: {} {}<br />'.format(
                'value',
                serialize_html_tag('<i>', str(__item.get('value_rating', ''))),
                '/ 10')
            + '{}: {} {}<br />'.format(
                'leverage',
                serialize_html_tag('<i>', str(__item.get('leverage_rating', ''))),
                '/ 10')
            + '{}: {} {}<br />'.format(
                'age',
                serialize_html_tag('<i>', str(__item.get('value_rating', ''))),
                'days')
            + '{}: {} {}<br />'.format(
                'url',
                serialize_html_tag(
                    tag='<a>',
                    value=str(self.context.get('domain', 'leboncoin.fr')),
                    attributes={'href': __item.get('url', '')}),
                ''))

        return __item
