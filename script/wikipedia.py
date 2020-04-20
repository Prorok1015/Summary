import wikipediaapi
from wiki.models import Categorys, Page, Sites
def createText(sections):
        text = ""

        for s in sections:
              heder = s.title
              body = s.text
              text = text + heder + " - " + body
              text = text + "/n"
        return text

def run():
        wiki_wiki = wikipediaapi.Wikipedia(
                language='ru',
                extract_format=wikipediaapi.ExtractFormat.WIKI
        )
        
        site = Sites.objects.get(SiteName = "Wikipedia")

        for category in Categorys.objects.all():
                if not category.Status:
                        cat = wiki_wiki.page("Категория:" + category.getCategory())

                        for c in cat.categorymembers.values():
                                page = wiki_wiki.page(c.title)
                                ltitle = page.title
                                lsummary = page.summary[0:179]
                                lurl = page.canonicalurl
                                ltext = createText(page.sections)
                                Page.objects.create(
                                        title = ltitle, 
                                        text = ltext, 
                                        url = site, 
                                        tag = category,
                                        summary = lsummary
                                        )
                        category.Status = True
                        category.save()


