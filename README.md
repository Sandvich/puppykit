# Puppykit
A repo for my website, [www.puppykit.org.uk](https://puppykit.org.uk)

Static, mostly a portfolio. Written almost entirely from scratch, using Pure CSS to make things a bit cleaner.  
The CSS and HTML for the navbar are from Pure's example [navbar](https://purecss.io/layouts/tucked-menu-vertical/).

## Contributing

Please feel free to contribute! For the most part, these things are related to me and therefore won't be appropriate for other people to correct, but on occasion that won't be the case.

Feel free to open issues or pull requests (request against the `corrections` branch, as that is where changes are staged until I'm ready to release them. `master` always represents the current state of the deployed code.)

## Running Locally

Running this website on your local system is easy if you have python 3.7.x or greater installed, as well as poetry. Simply run:

```bash
poetry install
poetry run python main.py
```

Then you can go to `localhost:5000` to see the website in action. Note: since the certs are done on my server, you'll be running in regular http, not https.

## Licensing

Please note: all code is licensed under Apache2, but content (including but not limited to images and PDFs) are not
available under this license. All content, unless marked otherwise, is released under
[CC BY-SA-NC 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) and copyright is retained.
