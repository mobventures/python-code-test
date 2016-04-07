from django.shortcuts import get_list_or_404, render
from stream.models import Stream

# Create your views here.
def show_stream(request):
    stream_list = get_list_or_404(Stream.objects.order_by('created_at'))
    current_stream = []  # Items that are not deleted

    print 'stream_data', stream_list

    for stream in stream_list:
        if(stream.tweet_item != None and stream.tweet_item.deleted == False):
            print stream.tweet_item.text
            print stream.tweet_item.deleted
            print type(stream.tweet_item)
            current_stream.append({'type': 'tweet', 'text': stream.tweet_item.text})

        elif(stream.photo_item != None and stream.photo_item.deleted == False):
            current_stream.append({'type': 'photo', 'image': stream.photo_item.image})

    obj = render(request, './stream.html', {'stream_data': current_stream})
    return obj
