function getMessage() {
    let message = fetch('/api/message/get').then(response => {
        return response.text();
    }).catch(error => {
        console.log('[Error]fetch.api.message.get:', error);
    });

    return message;
}