*** Settings ***
Resource                            base.robot

Test Setup                          Nova sessão
Test Teardown                       Encerra sessão

*** Test Cases ***
Login on TeamShift
    Enter on login page
    Insert email                    nefestor@outlook.com
    Insert password                 WLS2020qa
    Wait Until Page Contains        Como o TeamSHIFT funciona   timeout=10
    Check if user are logged        Tiago Coelho


*** Keywords ***
Insert email
    [Arguments]                     ${email}
    Wait Until Element Is Enabled   id:login-form__login
    Input Text                      id:login-form__login        ${email}
    Click Element                   class:js-login-form-submit

Enter on login page
    Click Element                   class:button-default

Insert password
    [Arguments]                     ${senha}
    Wait Until Element Is Enabled   id:login-form__password
    Input Text                      id:login-form__password     ${senha}
    Click Element                   class:js-login-form-submit

Check if user are logged
    [Arguments]                     ${user}
    Wait Until Page Contains        Tiago Coelho                 timeout=10
    Page Should Contain             Tiago Coelho