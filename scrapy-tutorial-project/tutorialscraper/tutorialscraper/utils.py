def specs_table_xpath(name):
    xpath = f'//tr[th[text()="{name}"]]/td/text()'
    return xpath
    
def specs_table_link_xpath(name):
    xpath = f'//tr[th[text()="{name}"]]/td/a/text()'
    return xpath