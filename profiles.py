from multiprocessing.reduction import AbstractReducer
import profile


class profiles(object):
    def __init__(self): #Initialize the PROFILES class.
        self.profile_col = []


    def new_profile(self, title):
        (self.profile_col).append(profile.profile(title))


    def new_ad(self, name, title):
        for p in self.profile_col:
            if(p.name == name):
                p.new_ad(title)

    def restore_ad(self, name, title, ad_id):
        for p in self.profile_col:
            if(p.name == name):
                p.restore_ad(title, ad_id)
    

    def profile_exists(self, name):
        for p in self.profile_col:
            if(p.name == name):
                return True
        return False


    def current_profiles(self):
        array = []
        for p in self.profile_col:
            array.append(p.name)
        return array

    def pick_profile(self, name):
        for p in self.profile_col:
            if(p.name == name):
                return p
    
    def current_ads(self):
        ads = []
        for p in self.profile_col:
            ads = ads + p.current_ads()
        return ads

    def ad_exist(self, ad_title):
        for p in self.profile_col:
            for a in p.ads_col:
                if(a.name == ad_title):
                    return True
        return False


    def pick_ad(self, ad_title):
        for p in self.profile_col:
            for a in p.ads_col:
                if(a.name == ad_title):
                    return a
        return 0

    def repost_ad(self, ad_title):
        for p in self.profile_col:
            for a in p.ads_col:
                if(a.name == ad_title):
                    p.repost_ad(ad_title)
                    self.database()
                    return 0

    def repost_add_ads(self):
        ads = []
        for p in self.profile_col:
            for ad in p.ads_col:
                ads.append(ad)

        print(ads)
        

        for ad_temp in ads:
            self.repost_ad(ad_temp.name)


    def delete_ad(self, ad_title):
        for p in self.profile_col:
            for a in p.ads_col:
                if(a.name == ad_title):
                    p.delete_ad(ad_title)

    def database(self):
        ads = []
        for profile in self.profile_col:
            for ad in profile.ads_col:
                temp = profile.name + " " + ad.name + " " + ad.ad_id + "\n"
                ads.append(temp)
        file = open('database', 'w')
        for line in ads:
            file.write(line)
        file.close()

    def restore(self):
        file = open('database', 'r')
        ads = file.read().splitlines()
        for ad in ads:
            ad = ad.split()
            if(not self.profile_exists(ad[0])):
                self.new_profile(ad[0])
            self.restore_ad(ad[0],ad[1],ad[2])
            
