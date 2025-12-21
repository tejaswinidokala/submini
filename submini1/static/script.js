function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let cookie of cookies) {
                    cookie = cookie.trim();
                    if (cookie.startsWith(name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }

function saveNoteToBackend(title, content, noteElement) {
        fetch('/api/save_note/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({ title: title, content: content })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Save failed');
                }
                return response.json();
            })
            .then(data => {
                if (data.status === 'success') {
                    noteElement.remove();  // Remove from index after saving
                } else {
                    alert('Save failed: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }

       