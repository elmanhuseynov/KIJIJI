import profiles
import chrome

print("Welcome to Kijiji Manager") #Simple intro.

input_action = "0" #Define string input_action as 0.
my_profiles = profiles.profiles() #Create object ADS where all current ads are stored.

while (input_action != "exit"): #Loop so that the program doesn't close after one repost or deletion

    print("Post or Repost all or Delete or Current or Exit?") #Simple text to console
    input_action = input() #Get input from user, to either delete or repost an ad.
    print("USER ENTERED: "+ input_action) #Print previus input


    if(input_action == "post" or input_action == "post " or input_action == "Post" or input_action == "Post "): #If used enters post, continue here.
        print("What ad to post?") #Simple text to console
        input_ad = input() #Get input from user, to select which ad to post.
        print("USER ENTERED: "+ input_ad + "\n") #Print previus input
    
        print("Which profile to use?")
        input_profile = input()
        print("USER ENTERED: "+ input_profile + "\n") #Print previus input

        if(my_profiles.profile_exists(input_profile)):
            print("Profile exists")
            my_profiles.new_ad(input_profile, input_ad)
            my_profiles.database()
        else:
            print("Profile does not exist")
            input_answer = str(input("Enter \"yes\" to make new profile, else press enter "))
            if(input_answer == "yes"):
                my_profiles.new_profile(input_profile)
                my_profiles.new_ad(input_profile, input_ad)
                my_profiles.database()




    elif(input_action == "repost" or input_action == "Repost" or input_action == "REPOST" or input_action == "repost "):
        print("Which ad to repost") #Simple text to console
        input_ad = input() #Get input from user, to select which ad to repost
        if(input_ad == "all"): 
            my_profiles.repost_add_ads() #Calling function to repost all ads.
            my_profiles.database()
        else:
            my_profiles.repost_ad(input_ad) #Calling function repost gived ad.
            my_profiles.database()

    elif(input_action == "kijiji"):
        print("Which profile to use?")
        input_profile = input()
        print("USER ENTERED: "+ input_profile + "\n") #Print previus input
        chrome.kijiji(input_profile)


    elif(input_action == "delete"):
        print("Which ad to delete?") #Simple text to console
        input_ad = str(input()) #Get input from user, to select which ad to delete.

        if(my_profiles.ad_exist(input_ad)):
            print("ad exists")
            my_profiles.delete_ad(input_ad)
            my_profiles.database()
            
        else:
            print("ad does not exist")
    
    elif(input_action == "load"):
        print("LOADING AFTER RESTART")
        my_profiles.restore()


    elif(input_action == "current" or input_action == "Current" or input_action == "CURRENT"): 
        print(my_profiles.current_ads()) #print current ads.

    elif(input_action == "exit" or input_action == "Exit" or input_action == "EXIT"):
        print("Thanks for using KIJIJI MANAGER")