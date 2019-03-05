from django.core.cache import cache
from micawber.providers import Provider, ProviderRegistry

oembed_providers = ProviderRegistry(cache)

oembed_providers.register(
    r'http://\S*imgur\.com/\S+',
    Provider('http://api.imgur.com/oembed')
),
oembed_providers.register(
    r'https?://\S*?flickr.com/\S+',
    Provider('https://www.flickr.com/services/oembed/')
)
oembed_providers.register(
    r'https?://flic\.kr/\S*',
    Provider('https://www.flickr.com/services/oembed/')
)
oembed_providers.register(
    r'http://i\S*.photobucket.com/albums/\S+',
    Provider('http://photobucket.com/oembed')
)
oembed_providers.register(
    r'http://gi\S*.photobucket.com/groups/\S+',
    Provider('http://photobucket.com/oembed')
)
oembed_providers.register(
    r'https://\S*?soundcloud.com/\S+',
    Provider('http://soundcloud.com/oembed')
)
oembed_providers.register(
    r'http://vimeo.com/\S+',
    Provider('http://vimeo.com/api/oembed.json')
)
oembed_providers.register(
    r'https://vimeo.com/\S+',
    Provider('https://vimeo.com/api/oembed.json')
)
oembed_providers.register(
    r'http://(\S*.)?youtu(\.be/|be\.com/watch)\S+',
    Provider('http://www.youtube.com/oembed')
)
oembed_providers.register(
    r'https://(\S*.)?youtu(\.be/|be\.com/watch)\S+',
    Provider('http://www.youtube.com/oembed?scheme=https&')
)
oembed_providers.register(
    r'https?://www.instagr(\.am|am\.com)/p/\S+',
    Provider('http://api.instagram.com/oembed')
)
oembed_providers.register(
    r'https?://www.facebook.com/\S+/videos/\S+',
    Provider('https://www.facebook.com/plugins/video/oembed.json')
)
oembed_providers.register(
    r'https?://www.facebook.com/video.php\?(id|v)=\S+',
    Provider('https://www.facebook.com/plugins/video/oembed.json')
)
