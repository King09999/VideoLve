echo "Cloning Repo, Please Wait..."
git clone -b master https://github.com/King09999/VideoLve /VideoPlayerBot
cd /VideoPlayerBot
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 main.py
