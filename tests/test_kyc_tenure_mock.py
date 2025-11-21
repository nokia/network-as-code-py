from datetime import datetime, timedelta, timezone, date

def test_kyc_tenure_returns_true(httpx_mock, client):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/kyc-tenure/kyc-tenure/v0.1/check-tenure"
    
    mock_response = {
        "tenureDateCheck": True,
        "contractType": "PAYG",
        }
            
    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "+99999991000",
            "tenureDate": "2023-09-18"
            })
                
    result = client.kyc.check_tenure(
            phone_number="+99999991000",
            tenure_date="2023-09-18"
            )
    
    assert result.tenure_date_check is True
    assert result.contract_type == "PAYG"

def test_kyc_tenure_with_date_object(httpx_mock, client):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/kyc-tenure/kyc-tenure/v0.1/check-tenure"
    
    mock_response = {
        "tenureDateCheck": True,
        "contractType": "PAYG",
        }
            
    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "+99999991000",
            "tenureDate": "2024-11-19"
            })
                
    result = client.kyc.check_tenure(
            phone_number="+99999991000",
            tenure_date=date(2024, 11, 19)
            )
    
    assert result.tenure_date_check is True
    assert result.contract_type == "PAYG"

def test_kyc_tenure_returns_false(httpx_mock, client):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/kyc-tenure/kyc-tenure/v0.1/check-tenure"
    
    mock_response = {
        "tenureDateCheck": False,
        }
            
    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "+99999991000",
            "tenureDate": "2023-09-18"
            })
                
    result = client.kyc.check_tenure(
            phone_number="+99999991000",
            tenure_date="2023-09-18"
            )
    
    assert result.tenure_date_check is False


def test_kyc_tenure_no_contract_type(httpx_mock, client):
    url = f"https://network-as-code.p-eu.rapidapi.com/passthrough/camara/v1/kyc-tenure/kyc-tenure/v0.1/check-tenure"
    
    mock_response = {
        "tenureDateCheck": True,
        }
            
    httpx_mock.add_response(
        url=url, 
        method='POST', 
        json=mock_response,
        match_json={
            "phoneNumber": "+99999991000",
            "tenureDate": "2023-09-18"
            })
                
    result = client.kyc.check_tenure(
            phone_number="+99999991000",
            tenure_date="2023-09-18"
            )
    
    assert result.tenure_date_check is True
    assert result.contract_type is None

