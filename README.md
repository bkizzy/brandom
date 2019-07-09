# brandom
My take on making a /dev/random clone. Exploring the concepts related to generating entropy.

# How it works
When run this python script creates an entropy pool file called 'brandom' which contains a series of random bytes sourced from random.org's cosmic noise antenna. When the full poolsize is reached, the file is overwritten again with new values, this way we always have fresh random bytes in the file.

# How to run it
>>nohup python brandom.py > log.out

# How to test it

>> cat brandom

get a 4 byte unsigned integer using the od command:

>>od -vAn -N4 -tu4 < brandom

NOTE:

-- with current settings the file refreshes 1000 bytes every 1/4 of second sequentially from beggining to end, so you will get a new number from the beginning of the file only once every 4-5 seconds
-- This is scrapping random.org so they will shut you down after a few runs, the file will just be static after that

# Why do it this way?

This was a time boxed experiment for me to explore how this kind of thing is done. random.org's service could be switched out with any source of random noise. /dev/random used device drivers, wifi APs in range could be another option, disk seek, bandwidth used by processes, etc. Anything that can provide an unpredictable source of randomness would do.

I used a seperate poolfile following the model set by /dev/random incase the source of entropy is slower than the service producing the random bytes

# TODO

-- create a device interface to the poolfile so it can serve the requested bytes and then truncate and relace them. This will allow every call to retrieve a random number and the client wouldn't need to manage the seek inside the file themselves

-- switch out the source of the randomness so it is more secure (not transmitted clear text) and preferrably local to the machine (doesn't require a network connection)
