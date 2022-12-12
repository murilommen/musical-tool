# Musical Tool - Backend

This repository is dedicated to host 2 API endpoints for a Front End application that will run a Music Analysis between two opposite 
"directions" in an Analysis Spectrum, such as Sustain/Improvisation, etc. 

## Database

The Database used for this application is a NoSQL MongoDB, that is hosted in the cloud at [www.mongodb.com](www.mongodb.com)

## API Documentation

The API documentations and testing Endpoints can be found [here](https://d8gfn7.deta.dev/docs). 

- **/analysis**: Is a *POST* endpoint to send an Analysis Object to the Database
- **/musics**: Is a *GET* endpoint to get the available musics from the `musics.json` file

>**IMPORTANT**: Note that if you use the POST endpoint you will have a new document created in the Database, and this can lead to a poor 
>data quality afterwards, so use it with caution!

## Editing the Musics list

In order to edit the available musics in the FrontEnd app, you should modify the `musics.json` file, located in the root of this repo. 
If you wish to add a new music, simply add a new object at the end, following this same structure as stated below.

```json
{
    "analysis_list": [
        {
            "music": "Performance1_G1",
            "path": "1pSXTLJ2WZVTqvlj4THgOImalzLA_SWcX"
        },
        {
            "music": "Performance1_G2",
            "path": "1E_bTyTVMjlB7AOfj4ZW2clLL4Du9LthP"
        }
    ]
}
```

The `path` argument should contain the music ID, which is the same as the one that appears in an **OPEN SHAREABLE** link from Google Drive.

## Contributing 

Feel free to open a Pull Request if you find anything 

## Foreseen Improvements
- [ ] API Validations for the `musics.json` document
