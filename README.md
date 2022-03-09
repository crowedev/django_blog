# About
This project serves as a Landing page for personal website www.crowe.dev and includes a Django Blog demo.

# Django Blog
This Blog project is written in Python utilizing the Django Framework. It serves as an exploration for a few tech stack choices, opting to replace the default sqlite DBs with postgres.  It includes simple standard blog functionality you'd expect, including: 
* User Registration (Open for public demo)
* Uploading Custom Re-Sized Avatars to replace defaults
* Creating, Editing, and Deleting Blog Posts
* Filtering Posts by User in the Feed
* Pagination of Blog Posts in the Feed

It is deployed to an AWS EC2 by means of a Gunicorn server utilizing Nginx as a reverse proxy.  The full website can be viewed and demo'd at https://crowe.dev/blog-home .
