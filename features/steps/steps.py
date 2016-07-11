from behaving.web.steps import *
from behaving.sms.steps import *
from behaving.mail.steps import *
from behaving.notifications.gcm.steps import *
from behaving.personas.steps import *
from behaving.personas.persona import persona_vars

@when(u'I login to Atmosphere')
@persona_vars
def i_login_to_atmo(context):
    context.execute_steps(u'''
        When I visit "$Atmosphere"
        And I press "Login"
        And I fill in "username" with "$username"
        And I fill in "password" with "$password"
        And I press "LOGIN"
    ''')

@step(u'I type "{value}" to class "{klass}"')
@persona_vars
def i_type_to_class(context, klass, value):
    name = "temp_form_name"
    assert context.browser.evaluate_script("document.getElementsByClassName('%s')[0].name = '%s'" % (klass, name)), \
        u'Element not found or could not set name'
    for key in context.browser.type(name, value, slowly=True):
        assert key

@step(u'I type slowly "{value}" to "{index}" index of class "{klass}"')
@persona_vars
def i_type_to_class(context, klass, value, index):
    name = "temp_form_name" + str(index)
    assert context.browser.evaluate_script("document.getElementsByClassName('%s')[%s].name = '%s'" % (klass, index, name)), \
        u'Element not found or could not set name'
    for key in context.browser.type(name, value, slowly=True):
        assert key

@step(u'I ask for "{resources}" resources for "{reason}" reason')
@persona_vars
def i_request_resources(context, resources, reason):
    klass = "form-control" # this is the class for both of the textarea elements

    # fill in resources
    name1 = "resource-box"
    assert context.browser.evaluate_script("document.getElementsByClassName('%s')[0].name = '%s'" % (klass, name1)), \
        u'Element not found or could not set name'
    for key in context.browser.type(name1, resources, slowly=True):
        assert key

    # fill in request reason
    name2 = "reason-box"
    assert context.browser.evaluate_script("document.getElementsByClassName('%s')[2].name = '%s'" % (klass, name2)), \
        u'Element not found or could not set name'
    for key in context.browser.type(name2, reason, slowly=True):
        assert key

@step(u'I press Report')
@persona_vars
def i_press_report(context):
    element = context.browser.find_by_xpath( "//*[@class='section-link']//span[contains(string(), 'Report')]")
    assert element, u'Element not found'
    element.first.click()

@step(u'I press Attach')
@persona_vars
def i_press_attach(context):
    element = context.browser.find_by_xpath( "//*[@class='section-link']//span[contains(string(), 'Attach')]")
    assert element, u'Element not found'
    element.first.click()

@step(u'I press Resume')
@persona_vars
def i_press_report(context):
    element = context.browser.find_by_xpath( "//*[@class='section-link']//span[contains(string(), 'Resume')]")
    assert element, u'Element not found'
    element.first.click()

@step(u'I press Delete')
@persona_vars
def i_press_report(context):
    element = context.browser.find_by_xpath( "//*[@class='section-link']//span[contains(string(), 'Delete')]")
    assert element, u'Element not found'
    element.first.click()

@step(u'I should see an element with class "{klass}"')
def i_see_element_with_class(context):
    assert context.browser.is_element_present_by_class(klass), u'Element not found'