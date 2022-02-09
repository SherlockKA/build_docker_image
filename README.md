### These steps help you to reproduce the code test<br>
**1. Clone project**
```
git clone https://github.com/SherlockKA/build_docker_image.git
```
**2. Create venv environment**
```
python3 -m venv build_docker_image_env
```
**3. Activate environment**
```
source build_docker_image_env/bin/activate
```
**4. Install libraries**
```
pip install -r requirements.txt
```
**5. Fix docker issue**
```
sudo chmod 666 /var/run/docker.sock
```
**6. Run build docker server**
```
make service_up
```
**7. Run client test**
```
make build_docker_image
```

P.S. Steps 6 and 7 must be executed from different processes <br>
