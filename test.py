import ad
import profile
import profiles

if __name__ == "__main__":
    print("TEST OF AD CLASS:")
    ad_1 = ad.ad("jeff", "CPU")
    print("Name of ad is " + ad_1.name)
    print(ad_1.ad_id)
    print('\n')

    print("TEST OF AD CLASS:")
    ad_2 = ad.ad("jeff", "PIZZA")
    print("Name of ad is " + ad_2.name)
    print(ad_2.ad_id)
    print('\n')


    print("TEST OF PROFILE CLASS:")
    profile_jeff = profile.profile("jeff")
    print("Name of profile is " + profile_jeff.name)
    print("Address of profile is ", profile_jeff)
    print('\n')

    print("TEST OF PROFILE CLASS:")
    profile_elvin = profile.profile("elvin")
    print("Name of profile is " + profile_elvin.name)
    print("Address of profile is ", profile_elvin)
    print('\n')

    print("TEST OF PROFILE CLASS:")
    print("ADDING AD CPU")
    profile_elvin.new_ad("CPU")
    print("ADDING AD PIZZA")
    profile_elvin.new_ad("PIZZA")
    print("Elvins current ads are ",profile_elvin.current_ads())
    print('\n')

    print("REMOVING AD PIZZA")
    profile_elvin.delete_ad("CPU")
    print("Elvins current ads are ",profile_elvin.current_ads())
    print('\n')

    print("TEST OF PROFILES CLASS")
    my_profiles = profiles.profiles()
    my_profiles.new_profile("jeff")
    my_profiles.new_profile("elvin")
    my_profiles.new_profile("jake")
    print("Current profiles are ", my_profiles.current_profiles())
    print("jeff exists? ", my_profiles.profile_exists("jeff"))
    print("Sarah exists? ", my_profiles.profile_exists("sarah"))
    print('\n')

    my_profiles.new_ad("jeff", "5600")
    print(my_profiles.pick_profile("jeff").current_ads())
    print(my_profiles.current_ads)
