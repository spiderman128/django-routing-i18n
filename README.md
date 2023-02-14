# Implement CMS with multi domains and translations

Django project with these requirements :



## 1. Project should serve multiple domains. Domain determinate which translation of objects should be used.
- en: en.superproject.localhost
- de: de.superproject.localhost
- fr: fr.superproject.localhost



A list of locales and domains should be provided in Django settings. Django translation mechanism should be used - translation.activate should be called depending on the domain.



## 2. Pages application (CMS like application):
- Page has slug, title and body (title and body should have translation in 3 languages: en, de, fr). Please, use your own solution.
- For example, if we open http://de.superproject.localhost/main we should see a page that has slug="main". We should see the title and the body for "de" locale.
- We should see Comments below Page.body.
- Pages should be managed from django admin.



## 3. News application:
- News item should have a slug, title and body (title and body with translations, like Page).
- News should be show with simple structure:
http://de.superproject.localhost/news/ - List of News items
http://de.superproject.localhost/news/SLUG - Detailed page for News item.
- On de.superproject.localhost we should see the title and body translated to "de" locale
- On News Item detail page Comments related to this News item.
- News items should be added using Django admin.



## 4. Comments application.
- Comment should be able to refer to any other object (Page, News). It should use some tools from Django contrib folder.
- Comment has "language", "body" and "created_at" fields.
- Language used to determinate for language to which this comment. For example, Comment to Page with slug="main" and language="de" should be shown only on "http://de.superproject.localhost/main".
- Comments should be added from admin. Let's skip functionality that allows adding comments by users from the site.