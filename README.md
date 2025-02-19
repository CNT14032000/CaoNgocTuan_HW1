I did homework 1 following these steps:
1. I wrote static_profile.html + style.css and 1 avatar.jpg to create my static profile page.
2. For the basic part, I wrote a basic_app.py file to serve the interface in a static folder using app.send_static_file().
3.For the advanced part. I created an additional index.html file based on static_profile.html and added {{ user.name }} and {{ user.bio }} as placeholders.
 Next, I used render_templat() to display index.html and the value from the user_info dictionary. I also used redirect(url_for('profile')) to redirect the route to '/profile'.
4.
