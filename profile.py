import time
import ad
from chrome import delete_ad

class profile(object):
    def __init__(self, name): #Initialize the PROFILE
        self.name = name
        self.ads_col = []


    def new_ad(self, title):
        (self.ads_col).append(ad.ad(self.name, title, 0))
    
    def restore_ad(self, title, ad_id):
        (self.ads_col).append(ad.ad(self.name,title,ad_id))

    def delete_ad(self, title):
        for ad in self.ads_col:
            if (ad.name == title):
                print("FOUND THE AD, DELETING NOW", ad.name)
                ad.delete_ad()
                self.ads_col.remove(ad)
                break


    def repost_ad(self, title):
        self.delete_ad(title)
        self.new_ad(title)

    def repost_all(self):
        length = len(self.ads_col)
        for i in range(length):
            self.repost_ad((self.ads_col[0]).name)

    def current_ads(self):
        titles = []
        for ad in self.ads_col:
            titles.append(ad.name)
        return titles

