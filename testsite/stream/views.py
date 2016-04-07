from django.shortcuts import get_list_or_404, render
from stream.models import Stream
from django.conf import settings

# Create your views here.
def show_stream(request):
    stream_list = get_list_or_404(Stream.objects.order_by('created_at'))
    current_stream = []  # Items that are not deleted

    print 'stream_data', stream_list

    for stream in stream_list:

        # handle tweets
        if(stream.tweet_item != None and stream.tweet_item.deleted == False):
            current_stream.append({
                'type': 'tweet',
                'text': stream.tweet_item.text,
                'time': str(stream.created_at)})

        # handle photos
        elif(stream.photo_item != None and stream.photo_item.deleted == False):
            current_stream.append({
                'type': 'photo',
                'img_href': stream.photo_item.image.url,
                'time': str(stream.created_at)})

    # render HTML from template
    obj = render(request, './stream.html', {'stream_data': current_stream})
    return obj
