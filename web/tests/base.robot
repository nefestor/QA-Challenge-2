*** Settings ***
Library                         SeleniumLibrary

*** Variable ***
${url}                          https://teamshift-qa.crossknowledge.com/

*** Keywords ***
Nova sessão
    
    Open Browser                ${url}     firefox
    

Encerra sessão
    Capture Page Screenshot
    Close Browser