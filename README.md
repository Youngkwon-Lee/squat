Squat Tracker DApp

This project is a decentralized application (DApp) that tracks squat repetitions using Pose Estimation (Keypoint-RCNN) and stores the count on the Solana blockchain. Users who complete 30 squats per day receive a token reward.

📌 Features

Pose Estimation: Uses Keypoint-RCNN to count squats in real-time.

Blockchain Integration: Stores squat count on Solana and rewards tokens.

DApp Development: Frontend built with Vue.js, backend with Spring, and smart contracts in Rust (Anchor Framework).

📂 Project Structure

squat-tracker-dapp/
│── backend/                   # Solana Smart Contract (Rust + Anchor)
│── blockchain/                # Solana deployment & config
│── frontend/                  # Web-based UI (Vue.js + Web3.js)
│── pose-estimation/           # Squat tracking (Keypoint-RCNN)
│── README.md                  # Project documentation
│── .gitignore                 # Ignored files

🚀 Setup & Installation

1️⃣ Clone the Repository

git clone https://github.com/Youngkwon-Lee/squat.git
cd squat-tracker-dapp

2️⃣ Setup Virtual Environment (For Pose Estimation)

cd pose-estimation
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Install Frontend Dependencies

cd ../frontend
npm install

4️⃣ Install Solana & Anchor (For Smart Contract)

cd ../backend
sh -c "$(curl -sSfL https://release.solana.com/stable/install)"
cargo install --git https://github.com/coral-xyz/anchor anchor-cli --locked
anchor build

🎥 Running the Squat Tracker

Start Pose Estimation

cd pose-estimation
python pose_estimation_keypointrcnn.py

Start Frontend DApp

cd ../frontend
npm run dev

📜 License

This project is licensed under the MIT License.

📩 Contact

For any inquiries, contact Youngkwon Lee via GitHub.
