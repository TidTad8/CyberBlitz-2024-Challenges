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

# Flag
CyberBlitz{BIG_BOSS_MAN_JAKE'S_LEG}