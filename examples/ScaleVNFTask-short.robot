*** Settings ***
# Resource    variables.txt 
#Library    REST    http://${VNFM_HOST}:${VNFM_PORT} 
# ...        spec=SOL003-VNFLifecycleManagement-API.yaml
#Library    DependencyLibrary
#Library    OperatingSystem

*** Test Cases ***
Scale a vnfInstance
    [Documentation]    Test ID: 9.8.7.6.5
    ...    Test Name: Scale VNF The POST method scales a VNF instance.. 
    ...    Another key: The operation cannot be executed currently, due to a conflict with the state of the VNF instance resource. 
    ...    Applicability: Typically, this is due to the fact that the VNF instance resource is in NOT-INSTANTIATED state, or that another lifecycle management operation is ongoing. 
    ...    Post-conditions: The response body shall contain a ProblemDetails structure, in which the detail attribute should convey more information about the error.
    Log    Trying to scale a vnf Instance
    Set Headers  {"Accept":"${ACCEPT}"}  
    Set Headers  {"Content-Type": "${CONTENT_TYPE}"}
    Run Keyword If    ${AUTH_USAGE} == 1    Set Headers    {"Authorization":"${AUTHORIZATION}"}
    ${body}=    Get File    json/scaleVnfRequest.json
    Post    ${apiRoot}/${apiName}/${apiVersion}/vnf_instances/${vnfInstanceId}/scale    ${body}
    Integer    response status    202
    Log    Status code validated

Scale a vnfInstance Conflict (Not-Instantiated)
    # TODO: Need to set the pre-condition of the test. VNF instance shall be in NOT-INSTANTIATED state
    [Documentation]    Test Name: Conflict. 
    ...    Reference: The operation cannot be executed currently, due to a conflict with the state of the VNF instance resource. 
    ...    Applicability: Typically, this is due to the fact that the VNF instance resource is in NOT-INSTANTIATED state, or that another lifecycle management operation is ongoing. 
    ...    Task: The response body shall contain a ProblemDetails structure, in which the detail attribute should convey more information about the error.
    [Setup]    Check resource not instantiated
    Log    Trying to Scale a vnf Instance
    Set Headers  {"Accept":"${ACCEPT}"}  
    Set Headers  {"Content-Type": "${CONTENT_TYPE}"}
    Run Keyword If    ${AUTH_USAGE} == 1    Set Headers    {"Authorization":"${AUTHORIZATION}"}
    ${body}=    Get File    json/scaleVnfRequest.json
    Post    ${apiRoot}/${apiName}/${apiVersion}/vnf_instances/${vnfInstanceId}/scale    ${body}
    Output    response
    Integer    response status    409
    Log    Status code validated
