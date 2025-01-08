let map;
let marker;
const locationInfoDiv = document.getElementById('location-info');

function initMap() {
    
    const defaultlocation = {lat: 34.7573, lng: 127.6643 }

    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 34.7573, lng: 127.6643 },
        zoom: 15
    });

    marker = new google.maps.Marker({
        position: defaultlocation,
        map: map,
        title: '현재 위치'
    });
}

function getCurrentLocation() {
    if(!navigator.geolocation) {
        updateStatus('이 브라우저에서는 위치 정보를 지원하지 않습니다.');
        return;
    }

    updateStatus('위치 정보를 가져오는 중...');

    const options = {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0
    };

    navigator.geolocation.getCurrentPosition(
        (position) => {
            const pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            map.setCenter(pos);
            marker.setPosition(pos);
            updateStatus(`위도: ${pos.lat.toFixed(6)}, 경도: ${pos.lng.toFixed(6)}`);
        },
        (error) => {
            let errorMessage;
            switch(error.code) {
                case error.PERMISSION_DENIED:
                    errorMessage = "위치 정보 접근이 거부되었습니다. 브라우저의 위치 정보 권한을 확인하세요.";
                    break;
                case error.POSITION_UNAVAILABLE:
                    errorMessage = "위치 정보를 사용할 수 없습니다.";
                    break;
                case error.TIMEOUT:
                    errorMessage = "위치 정보 요청이 시간 초과되었습니다.";
                    break;
                default:
                    errorMessage = "알 수 없는 오류가 발생했습니다.";
            }
            updateStatus(errorMessage);
        },
        options
    );
}

/**
 * 상태 메시지를 화면에 업데이트하는 함수
 * @param {string} message - 표시할 메시지
 */
function updateStatus(message) {
    locationInfoDiv.textContent = message;
}