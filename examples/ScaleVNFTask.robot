*** Settings ***
# Resource    variables.txt 
#Library    REST    http://${VNFM_HOST}:${VNFM_PORT} 
# ...        spec=SOL003-VNFLifecycleManagement-API.yaml
#Library    DependencyLibrary
#Library    OperatingSystem

*** Test Cases ***
Scale a vnfInstance
    [Documentation]    Test Name: Scale VNF The POST method scales a VNF instance.. 
    ...    Another: The operation cannot be executed currently, due to a conflict with the state of the VNF instance resource. 
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
    [Documentation]    Prova: Conflict. 
    ...    Another: The operation cannot be executed currently, due to a conflict with the state of the VNF instance resource. 
    ...    Applicability: Typically, this is due to the fact that the VNF instance resource is in NOT-INSTANTIATED state, or that another lifecycle management operation is ongoing. 
    ...    The response body shall contain a ProblemDetails structure, in which the detail attribute should convey more information about the error.
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

Scale a vnfInstance Conflict (parallel LCM operation)
    # TODO: Need to set the pre-condition of the test
    [Documentation]    Example: Conflict
    ...    Maybe: The operation cannot be executed currently, due to a conflict with the state of the VNF instance resource. 
    ...    Typically, this is due to the fact that the VNF instance resource is in NOT-INSTANTIATED state, or that another lifecycle management operation is ongoing. 
    ...    The response body shall contain a ProblemDetails structure, in which the detail attribute should convey more information about the error.
    [Setup]    Launch another LCM operation
    log    Trying to Scale a vnf Instance
    Set Headers    {"Accept":"${ACCEPT}"}  
    Set Headers    {"Content-Type": "${CONTENT_TYPE}"}
    Run Keyword If    ${AUTH_USAGE} == 1    Set Headers    {"Authorization":"${AUTHORIZATION}"}
    ${body}=    Get File    json/scaleVnfRequest.json
    Post    ${apiRoot}/${apiName}/${apiVersion}/vnf_instances/${vnfInstanceId}/scale    ${body}
    Log    Validate Status code
    Output    response
    Integer    response status    409
    [Teardown]    #We cannot know if the "scale" operation is finished easily because the 202 indicates only whether the operation has been accepted, not whether the operation has been finished
    
Scale a vnfInstance Not Found
    # TODO: Need to create a vnfInstance which's instantiatedVnfInfo.scaleStatus is absent
    [Documentation]    Not Found
    ...    Error: The API producer did not find a current representation for the target resource or is not willing to disclose that one exists. 
    ...    Specifically in case of this task resource, the response code 404 shall also returned if the task is not supported for the VNF instance represented by the parent resource, which means that the task resource consequently does not exist. 
    ...    In this case, the response body shall be present, and shall contain a ProblemDetails structure, in which the detail attribute shall convey more information about the error.
    [Setup]    Check scale not supported
    Log    Trying to scale a vnf Instance, not exist
    Set Headers  {"Accept":"${ACCEPT}"}  
    Set Headers  {"Content-Type": "${CONTENT_TYPE}"}
    Run Keyword If    ${AUTH_USAGE} == 1    Set Headers    {"Authorization":"${AUTHORIZATION}"}
    ${body}=    Get File    json/scaleVnfRequest.json
    Post    ${apiRoot}/${apiName}/${apiVersion}/vnf_instances/${vnfInstanceId}/scale    ${body}
    Integer    response status    404
    Log    Status code validated
   
    
GET Scale VNFInstance - Method not implemented
    log    Trying to perform a GET. This method should not be implemented
    Run Keyword If    ${AUTH_USAGE} == 1    Set Headers    {"Authorization":"${AUTHORIZATION}"}
    Get    ${apiRoot}/${apiName}/${apiVersion}/vnf_instances/${vnfInstanceId}/scale    
    Log    Validate Status code
    Output    response
    Integer    response status    405

PUT Scale VNFInstance - Method not implemented
    log    Trying to perform a PUT. This method should not be implemented
    Run Keyword If    ${AUTH_USAGE} == 1    Set Headers    {"Authorization":"${AUTHORIZATION}"}
    Put    ${apiRoot}/${apiName}/${apiVersion}/vnf_instances/${vnfInstanceId}/scale    
    Log    Validate Status code
    Output    response
    Integer    response status    405

PATCH Scale VNFInstance - Method not implemented
    log    Trying to perform a PATCH. This method should not be implemented
    Run Keyword If    ${AUTH_USAGE} == 1    Set Headers    {"Authorization":"${AUTHORIZATION}"}
    Patch    ${apiRoot}/${apiName}/${apiVersion}/vnf_instances/${vnfInstanceId}/scale    
    Log    Validate Status code
    Output    response
    Integer    response status    405
    
DELETE Scale VNFInstance - Method not implemented
    log    Trying to perform a DELETE. This method should not be implemented
    Run Keyword If    ${AUTH_USAGE} == 1    Set Headers    {"Authorization":"${AUTHORIZATION}"}
    Delete    ${apiRoot}/${apiName}/${apiVersion}/vnf_instances/${vnfInstanceId}/scale    
    Log    Validate Status code
    Output    response
    Integer    response status    405

*** Key words ***
Check resource existance
    Set Headers    {"Accept":"${ACCEPT}"}  
    Set Headers    {"Content-Type": "${CONTENT_TYPE}"}
    Run Keyword If    ${AUTH_USAGE} == 1    Set Headers    {"Authorization":"${AUTHORIZATION}"}
    Get    ${apiRoot}/${apiName}/${apiVersion}/vnf_instances/${vnfInstanceId} 
    Integer    response status    200

Check resource not instantiated
    Set Headers    {"Accept":"${ACCEPT}"}  
    Set Headers    {"Content-Type": "${CONTENT_TYPE}"}
    Run Keyword If    ${AUTH_USAGE} == 1    Set Headers    {"Authorization":"${AUTHORIZATION}"}
    Get    ${apiRoot}/${apiName}/${apiVersion}/vnf_instances/${vnfInstanceId} 
    String    response body instantiationState    NOT_INSTANTIATED

Check scale not supported
    Set Headers    {"Accept":"${ACCEPT}"}  
    Set Headers    {"Content-Type": "${CONTENT_TYPE}"}
    Run Keyword If    ${AUTH_USAGE} == 1    Set Headers    {"Authorization":"${AUTHORIZATION}"}
    Get    ${apiRoot}/${apiName}/${apiVersion}/vnf_instances/${vnfInstanceId} 
    Missing    response body instantiatedVnfInfo scaleStatus

Launch another LCM operation
    Set Headers  {"Accept":"${ACCEPT}"}  
    Set Headers  {"Content-Type": "${CONTENT_TYPE}"}
    Run Keyword If    ${AUTH_USAGE} == 1    Set Headers    {"Authorization":"${AUTHORIZATION}"}
    ${body}=    Get File    json/scaleVnfToLevelRequest.json
    Post    ${apiRoot}/${apiName}/${apiVersion}/vnf_instances/${vnfInstanceId}/scale_to_level    ${body}
    Integer    response status    202