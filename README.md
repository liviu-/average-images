# Average Pixels

## Overview
Command line tool which takes search terms as inputs, and outputs a JPEG combining multiple images related to the terms provided.

## Installation

    $ pip install average_pixels
    
## Configuration
The application uses [Bing Search API](https://www.microsoft.com/cognitive-services/en-us/bing-image-search-api) to search for images so it requires the user to have an API key activated for their search service. Once obtained, the key may be provided when prompted by the application, or in `~/.average_pixels_api`. The expected format is just the API string with no other characters in the file.

## Example usage:

    $ average_pixels "black cats"
    
![black_cats](average_pixels/outputs/black_cats.jpg)

    $ average_pixels "white cat"
    
![white_cat](average_pixels/outputs/white_cat.jpg)

    $ average_pixels "green field blue sky"
    
![green_field_blue_sky](average_pixels/outputs/green_field_blue_sky.jpg)

    $ average_pixels "just give me some random photo"

![just_give_me_some_random_photo](average_pixels/outputs/just_give_me_some_random_photo.jpg)

    $ average_pixels "no"

![just_give_me_some_random_photo](average_pixels/outputs/no.jpg)

    $ average_pixels "insects" --count 30

![just_give_me_some_random_photo](average_pixels/outputs/insects.jpg)
