I did homework 1 following these steps:
1. I wrote static_profile.html + style.css and 1 avatar.jpg to create my static profile page.
2. For the basic part, I wrote a basic_app.py file to serve the interface in a static folder using app.send_static_file().
3. For the advanced part. I created an additional index.html file based on static_profile.html and added {{ user.name }} and {{ user.bio }} as placeholders.
 Next, I used render_templat() to display index.html and the value from the user_info dictionary. I also used redirect(url_for('profile')) to redirect the route to '/profile'.
4. How to run:
   - Install Flask: pip install Flask
   - Run the application: Basic part: python basic_app.py, Advanced part: python adv_app.py
   - Open your browser and run: http://localhost:5000 or click the link on your terminal.

  You can view my profile in link github-page: [here](http://289236.osinthijacking.itmo.xyz/CaoNgocTuan_HW1/)
