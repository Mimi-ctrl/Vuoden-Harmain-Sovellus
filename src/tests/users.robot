*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page First

*** Test Cases ***
Register With Valid Username And Password
    Set Username  nimi
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Succeed

Can not Register With Too Short Username
    Set Username  ni
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Register Should Fail

Can not Register With Too Short Password
    Set Username  nimi
    Set Password  sa
    Set Password Confirmation  sa
    Submit Credentials
    Register Should Fail

Can not Register With Password Mismatch
    Set Username  nimi
    Set Password  salasana123
    Set Password Confirmation  salaminaama123
    Submit Credentials
    Register Should Fail With Message  Salasanat eivät ole samat

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password1  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password2  ${password}

Submit Credentials
    Click Button  Luo tunnus

Go To Register Page First
    Go To Register Page

Register Should Succeed
    Main Page Should Be Open

Register Should Fail
    Register Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${Message}

