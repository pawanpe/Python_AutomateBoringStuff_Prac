import bs4, requests

def price():
    res = requests.get("https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994")
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')

    links = soup.select('html.a-transition.a-transform.a-opacity.a-border-image.a-border-radius.a-box-shadow.a-text-stroke.a-text-shadow.-scrolling.a-transform3d.a-hires.a-gradients.a-local-storage.a-textarea-placeholder.a-input-placeholder.a-autofocus.a-webworker.a-history.a-geolocation.a-drag-drop.a-svg.a-canvas.a-video.a-audio.a-js.a-ws body.a-m-us.a-aui_107069-c.a-aui_51744-c.a-aui_57326-c.a-aui_72554-c.a-aui_accessibility_49860-c.a-aui_attr_validations_1_51371-c.a-aui_bolt_62845-c.a-aui_noopener_84118-t1.a-aui_ux_102912-c.a-aui_ux_59374-c.a-aui_ux_60000-c.a-aui_ux_92006-c.a-aui_ux_98513-c.a-dex_92889-c.a-meter-animate div#a-page div#dp.book.en_US div#dp-container.a-container div.a-fixed-left-grid div.a-fixed-left-grid-inner div#ppdFixedGridRightColumn.a-fixed-left-grid-col.a-col-right div#mediaTabsGroup.feature div#mediaTabsGroup.a-section.a-spacing-base div#mediaTabs_tabSetContainer.a-tab-container.a-spacing-none div#mediaTab_content_landing.a-box.a-box-tab.a-tab-content div.a-box-inner div#mediaAccordion.a-box-group.a-accordion.a-spacing-none div#newOfferAccordionRow.a-box.accordion-row div.a-box-inner.a-accordion-row-container form#addToCart.a-spacing-none.a-content div.a-accordion-row-a11y a.a-accordion-row.a-declarative.accordion-header h5 div.a-row div.a-column.a-span4.a-text-right.a-span-last span.a-size-medium.header-price.a-color-secondary')
    print(links)

    links2 = soup.select('a')
    print(len(links2))

    for index in range(len(links2)):
       curr = links2[index].attrs
       print(curr) #TODO: get href value from each in dict and launch webpage.


    if len(links) == 0:
        return 0
    else:
        return links[0].text.strip()

p = price()
print(p)
# for curr in links:
#     href = links.__getattribute__('href')
#     requests.get(href)
