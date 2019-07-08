*** Settings ***
Library           JSONSchemaLibrary    schemas/
Resource          environment/variables.txt    # Generic Parameters
Resource          environment/vnfPackageArtifacts.txt
Resource          VNFPackageManagementKeywords.robot 
Library           JSONLibrary
Library           REST    ${NFVO_SCHEMA}://${NFVO_HOST}:${NFVO_PORT}

*** Test Cases ***
GET Individual VNF Package Artifact
    [Documentation]    Test ID: 7.3.3.5.1
    ...    Test title: GET Individual VNF Package Artifact
    ...    Test objective: The objective is to test the retrieval of an individual VNF package artifact
    ...    Pre-conditions: One or more VNF packages are onboarded in the NFVO.
    ...    Reference: section 10.4.6.3.2 - SOL003 v2.4.1
    ...    Config ID: Config_prod_NFVO
    ...    Applicability: none
    ...    Post-Conditions: none
    GET Individual VNF Package Artifact
    Check HTTP Response Status Code Is    200


GET Individual VNF Package Artifact in octet stream format
    [Documentation]    Test ID: 7.3.3.5.2
    ...    Test title: GET Individual VNF Package Artifact in octet stream format
    ...    Test objective: The objective is to test the retrieval of an individual VNF package artifact when the NFVO cannot determine the artifact content type. The test performs a validation that the returned artifcat in is octet-stream format 
    ...    Pre-conditions: One or more VNF packages are onboarded in the NFVO.
    ...    Reference: section 10.4.6.3.2 - SOL003 v2.4.1
    ...    Config ID: Config_prod_NFVO
    ...    Applicability: The NFVO cannot determine the content type of the artifact
    ...    Post-Conditions: none
    GET Individual VNF Package Artifact in octet stream format
    Check HTTP Response Status Code Is    200
    Check HTTP Response Header Content-Type Is    application/octet-stream

GET Individual VNF Package Artifact with Range Request and NFVO supporting Range Requests
    [Documentation]    Test ID: 7.3.3.5.3
    ...    Test title: GET Individual VNF Package Artifact with Range Request and NFVO supporting Range Requests
    ...    Test objective: The objective is to test the retrieval of an individual VNF package artifact when using a range request to return single range of bytes from the file, with the NFVO supporting it. The test also perform a validation that returned content matches the issued range
    ...    Pre-conditions: One or more VNF packages are onboarded in the NFVO.
    ...    Reference: section 10.4.6.3.2 - SOL003 v2.4.1
    ...    Config ID: Config_prod_NFVO
    ...    Applicability: The NFVO supports range requests to return single range of bytes from the VNF package artifact
    ...    Post-Conditions: none
    GET Individual VNF Package Artifact with Range Request
    Check HTTP Response Status Code Is    206
    Check HTTP Response Header Content-Range Is Present and Matches the requested range
    Check HTTP Response Header Content-Length Is Present and Matches the requested range length

GET Individual VNF Package Artifact with Range Request and NFVO not supporting Range Requests
    [Documentation]    Test ID: 7.3.3.5.4
    ...    Test title: GET Individual VNF Package Artifact with Range Request and NFVO not supporting Range Requests
    ...    Test objective: The objective is to test that the retrieval of an individual VNF package artifact, when using a range request to return single range of bytes from the file and the NFVO not supporting it, returns the full VNF Package artifact.
    ...    Pre-conditions: One or more VNF packages are onboarded in the NFVO.
    ...    Reference: section 10.4.6.3.2 - SOL003 v2.4.1
    ...    Config ID: Config_prod_NFVO
    ...    Applicability: The NFVO does not support range requests to return single range of bytes from the VNF package artifact
    ...    Post-Conditions: none    
    GET Individual VNF Package Artifact with Range Request
    Check HTTP Response Status Code Is    200

GET Individual VNF Package Artifact with invalid Range Request
    [Documentation]    Test ID: 7.3.3.5.5
    ...    Test title: GET Individual VNF Package Artifact with invalid Range Request
    ...    Test objective: The objective is to test that the retrieval of an individual VNF package artifact fails when using a range request that does not match any available byte range in the file.
    ...    Pre-conditions: One or more VNF packages are onboarded in the NFVO.
    ...    Reference: section 10.4.6.3.2 - SOL003 v2.4.1
    ...    Config ID: Config_prod_NFVO
    ...    Applicability: The NFVO supports range requests to return single range of bytes from the VNF package artifact
    ...    Post-Conditions: none      
    GET Individual VNF Package Artifact with invalid Range Request
    Check HTTP Response Status Code Is    416

GET Individual VNF Package Artifact with invalid resource identifier
    [Documentation]    Test ID: 7.3.3.5.6
    ...    Test title: GET Individual VNF Package Artifact with invalid resource identifier
    ...    Test objective: The objective is to test that the retrieval of an individual VNF package artifact fails when using an invalid resource identifier
    ...    Pre-conditions: One or more VNF packages are onboarded in the NFVO.
    ...    Reference: section 10.4.6.3.2 - SOL003 v2.4.1
    ...    Config ID: Config_prod_NFVO
    ...    Applicability: none
    ...    Post-Conditions: none    
    GET Individual VNF Package Artifact with invalid resource identifier
    Check HTTP Response Status Code Is    404

GET Individual VNF Package Artifact with conflict due to onboarding state
    [Documentation]    Test ID: 7.3.3.5.7
    ...    Test title: GET Individual VNF Package Artifact with conflict due to onboarding state
    ...    Test objective: The objective is to test that the retrieval of an individual VNF package artifact fails due to a conflict when the VNF Package is not in onboarding state ONBOARDED in the NFVO. The test also performs a validation of the JSON schema validation of the failed operation HTTP response
    ...    Pre-conditions: The onboarding state of the VNF package for which the content is requested is different from ONBOARDED.
    ...    Reference: section 10.4.6.3.2 - SOL003 v2.4.1
    ...    Config ID: Config_prod_NFVO
    ...    Applicability: none
    ...    Post-Conditions: none   
    GET Artifact for VNF Package in onboarding state different from ONBOARDED
    Check HTTP Response Status Code Is    409
    Check HTTP Response Body Json Schema Is   ProblemDetails

POST Individual VNF Package Artifact - Method not implemented
    [Documentation]    Test ID: 7.3.3.5.8
    ...    Test title: POST Individual VNF Package Artifact - Method not implemented
    ...    Test objective: The objective is to test that POST method is not allowed to create new VNF Package artifact
    ...    Pre-conditions: none
    ...    Reference: section 10.4.6.3.1 - SOL003 v2.4.1
    ...    Config ID: Config_prod_NFVO
    ...    Applicability: none
    ...    Post-Conditions: none
    Send POST Request for individual VNF Package Artifact
    Check HTTP Response Status Code Is    405

PUT Individual VNF Package Artifact - Method not implemented
    [Documentation]    Test ID: 7.3.3.5.9
    ...    Test title: PUT Individual VNF Package Artifact - Method not implemented
    ...    Test objective: The objective is to test that PUT method is not allowed to modify a VNF Package artifact
    ...    Pre-conditions: One or more VNF packages are onboarded in the NFVO.
    ...    Reference: section 10.4.6.3.3 - SOL003 v2.4.1
    ...    Config ID: Config_prod_NFVO
    ...    Applicability: none
    ...    Post-Conditions: none
    Send PUT Request for individual VNF Package Artifact
    Check HTTP Response Status Code Is    405

PATCH Individual VNF Package Artifact - Method not implemented
    [Documentation]    Test ID: 7.3.3.5.10
    ...    Test title: PATCH Individual VNF Package Artifact - Method not implemented
    ...    Test objective: The objective is to test that PATCH  method is not allowed to update a VNF Package artifact
    ...    Pre-conditions: One or more VNF packages are onboarded in the NFVO.
    ...    Reference: section 10.4.6.3.4 - SOL003 v2.4.1
    ...    Config ID: Config_prod_NFVO
    ...    Applicability: none
    ...    Post-Conditions: none
    Send PATCH Request for individual VNF Package Artifact
    Check HTTP Response Status Code Is    405

DELETE Individual VNF Package Artifact - Method not implemented
    [Documentation]    Test ID: 7.3.3.5.11
    ...    Test title: DELETE Individual VNF Package Artifact - Method not implemented
    ...    Test objective: The objective is to test that DELETE  method is not allowed to delete a VNF Package artifact
    ...    Pre-conditions: One or more VNF packages are onboarded in the NFVO.
    ...    Reference: section 10.4.6.3.5 - SOL003 v2.4.1
    ...    Config ID: Config_prod_NFVO
    ...    Applicability: none
    ...    Post-Conditions: The VNF Package artifact is not deleted by the failed operation
    Send DELETE Request for individual VNF Package Artifact
    Check HTTP Response Status Code Is    405
    Check Postcondition VNF Package Artifact Exist

