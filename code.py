import instaloader
import bitlyshortener
from IPython.display import Markdown, display
def printmd(string):
    display(Markdown(string))
import fontstyle
tokens_pool = [*insert bitly token*]
shortener = bitlyshortener.Shortener(tokens=tokens_pool, max_cache_size=256)
bot = instaloader.Instaloader()


def preparespecificposts(username, index):
    profile=instaloader.Profile.from_username(bot.context, username)
    username=profile.username
    format_username="<i>" + "by " + username + "</i>"
    printmd(format_username)
    print('\n')
    # get all posts in a generator object
    posts=profile.get_posts()
    #iterate and downlaod
    for postnumber, post in enumerate(posts,1):
        if postnumber==index:
            bot.download_post(post,target=f"{username} promo")
            shortcode = post.shortcode
            print('\n')
            print('caption: ' , post.caption)
            print('\n')
            break
    long_urls = ['https://www.instagram.com/p/' + shortcode]
    print('link: ' , shortener.shorten_urls(long_urls))
    
def preparesavedposts(index):
    bot.login(*insert username*, *insert password*)
    profile=instaloader.Profile.from_username(bot.context, *insert username*)
    posts=profile.get_saved_posts()
    for postnumber, post in enumerate(posts,0):
        if postnumber<index:
            bot.download_post(post,target="saved posts tests")
            long_urls=[]
            shortcode = post.shortcode
            long_urls=['https://www.instagram.com/p/' + shortcode]
            username=post.owner_username
            format_username = "<i>" + "by " + username + "</i>"
            print('\n')
            printmd(format_username)
            print('\n')
            print('caption: ' , post.caption)
            print('\n')
            print('link: ' , shortener.shorten_urls(long_urls))
            print('\n')
