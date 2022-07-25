# My portfolio at [**lukepomeroy.co.uk**](https://lukepomeroy.co.uk)

My portfolio website was built using Django and a modified HTML5/CSS3 template from [*StyleShout*](https://www.styleshout.com/free-templates/kards/).
The projects and CV featured on this site are stored in a SQLite database and are displayed via the Django ORM and template engine.
My portfolio website is currently hosted on an Oracle Cloud Instance (via an Standard A1 Flex VM).

I've added a few new features to the StyleShout template including:
- Using the built-in Django send_mail functionality and a Django view to send emails rather than a sendMail.php file and sendmail.
- Addition of jquery scroll events for projects gallery to improve the experience for mobile device users (using [*jquery.scrollex*](https://github.com/ajlkn/jquery.scrollex)).

## ToDo
- [ ] Create Django Contact Form, rather than form submitted via Ajax and validated in views.py
- [ ] Add multiple images in a gallery to projects pop-up modal
- [ ] Add separate project pages
