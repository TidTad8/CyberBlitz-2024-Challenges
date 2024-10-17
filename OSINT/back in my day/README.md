Creator: <a href="https://github.com/TidTad8">@TidTad8</a>

# Challenge Description
Back in my day, this was one of my favorite songs. 

But I think these guys did it better than the original 25 years later.

Flag format in full capital letters: CyberBlitz{SONG_NAME_SINGER/BAND_NAME}

# Solution
By listening to the lyrics, can find out the song is Big Boss Man by Jimmy Reed in 1960

Audio search does not return any results

Based on the challenge description, search wayback machine for a cover in 1985 (1960 + 25) with the following advanced query:

```(big boss man) AND date:[1985-01-01 TO 1985-12-01]```

Looking through the top few results, found the following: https://archive.org/details/JakesLeg-AmusingOurselvesToDeathCassetteEP/

Sure enough, this is the cover album including Big Boss Man as the first song

# Hint: The name of this album should be Bats & Bugs Music

Even though Internet Archive is down due to the recent DOS, we can still attempt to do a Google search as its index is based on a snapshot of the site from when it was last crawled. Finding out the song name from the audio and with the challenge description, use a simple Google search query:

```"internet archive" "1985" "big boss man"```

Under Images, we see one of the first few results show an image with the same description as the hint, which reveals the band name:

![image](https://github.com/user-attachments/assets/5a82ef18-6d00-46dd-a170-bebb66a09a92)

# Flag
CyberBlitz{BIG_BOSS_MAN_JAKE'S_LEG}
