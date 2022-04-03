import chrome



class ad(object):
    def __init__(self,profile, name, ad_id): #Initialize the AD
            
        self.profile = profile
        self.name = name
        if(ad_id==0):
            #self.ad_id = "https://www.kijiji.ca/v-view-details.html?adId=1607966413fdfdfd"
            self.ad_id = chrome.post_ad(self.profile, self.name)
            word = self.ad_id[0:4]
            for i in range(4, (len(self.ad_id))):
                if(word == "adId"):
                    word =  word + self.ad_id[i:i+11]
                    break
                word = word[1:] + self.ad_id[i]
            self.ad_id = word
        else:
            self.ad_id = ad_id

    
    
        

    def delete_ad(self):
        #print("deleting ad", self.ad_id)
        chrome.delete_ad(self.profile, self.ad_id)