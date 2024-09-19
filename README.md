# qa-test - Kubernetes Deployment and Automated Testing

## Prerequisites:
- Python 3.x
- Minikube for running Kubernetes locally

## Kubernetes Setup:

1. **Clone the repository**:
   ```powershell
   git clone https://github.com/Vengatesh-m/qa-test.git
   cd qa-test/Deployment

2. **Deploy backend and frontend services**:
    kubectl apply -f backend-deployment.yaml
    kubectl apply -f frontend-deployment.yaml

3. **Expose the services**:
    kubectl expose deployment backend-deployment --type=ClusterIP --port=8081
    kubectl expose deployment frontend-deployment --type=LoadBalancer --port=8080

4. **Verify that the frontend is reachable by accessing the Minikube URL or by running**:
    minikube service frontend-deployment

---

## Automated Testing:

1. Run the test script:
    ```powershell
    cd C:\Users\sudha\qa-test\accuknox_Assessment
    python test_selenium.py
2. Output:
    Test is passed         

---

### Deliverables:

1. **Test Script**:
   - Ensure the `test_selenium.py` is included in your repository.

2. **Public GitHub Repository**:
   Push the repository to GitHub and make it public:
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin 
   git push -u origin main
