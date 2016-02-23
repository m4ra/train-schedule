from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse

class LatestEntriesFeed(Feed):
    title = "Weather news"
    link = "/sitenews/"
    description = "Weather updates"

    def items(self):
        return NewsItem.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title




