*** Settings ***
Resource  resource.robot
Suite Setup  Open Browser And Reset Database
Suite Teardown  Close Browser
Test Setup  Go To Main Page First

*** Test Cases ***

Add and view Citation After Registering
    Go To Register Page
    Set Username  kayttaja1
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Input Citation Info  Herra Hakkarainen  Mauri Kunnas  2001
    Submit Citation
    Output Should Contain  Herra Hakkarainen


*** Keywords ***

Input Citation Info
    [Arguments]  ${title}  ${author}  ${year}
    Input text  title  ${title}
    Input text  author  ${author}
    Input text  year  ${year}

Submit Citation
    Click Button  Lisää viite
    
Go To Register Page
    Click Link  Luo uusi tunnus

Go To Main Page First
    Go To Main Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password1  ${password}

Set Password Main Page
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password2  ${password}

Submit Credentials
    Click Button  Luo tunnus

Output Should Contain
    [Arguments]  ${message}
    Page Should Contain  ${Message}
