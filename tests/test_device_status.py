from network_as_code.models.device_status import ConnectivitySubscription


def test_creating_connectivity_subscription_with_notification(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    subscription = client.connectivity.subscribe(
        device=device, 
        max_num_of_reports=5, 
        notification_url="https://example.com/notifications", 
        notification_auth_token="c8974e592c2fa383d4a3960714"
    )

    subscription.delete()

def test_getting_connectivity(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    connectivity_subscription = client.connectivity.subscribe(
        device=device, 
        max_num_of_reports=5, 
        notification_url="https://example.com/notifications", 
        notification_auth_token="c8974e592c2fa383d4a3960714"
    )

    response = client.connectivity.get_subscription(connectivity_subscription.id)

    assert response.device == device

    connectivity_subscription.delete()

def test_delete_connectivity(client):
    device = client.devices.get("testuser@open5glab.net", ip = "1.1.1.2")

    connectivity_subscription = client.connectivity.subscribe(
        device=device, 
        max_num_of_reports=5, 
        notification_url="https://example.com/notifications", 
        notification_auth_token="c8974e592c2fa383d4a3960714"
    )

    connectivity_subscription.delete()

    response = device.get_connectivity(connectivity_subscription.id) 

    assert response == None # Should return a null response due to connectivity being deleted already
