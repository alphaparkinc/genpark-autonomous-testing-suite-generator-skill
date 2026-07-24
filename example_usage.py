from client import AutonomousTestingSuiteGeneratorClient

def main():
    client = AutonomousTestingSuiteGeneratorClient()
    telemetry = [
        {"action": "click", "target": "#submit-order-btn"},
        {"action": "type", "target": "input[name='coupon']"}
    ]
    res = client.generate_tests(telemetry)
    print(f"Coverage Estimate: {res['coverage_estimate_pct']}%")
    print("Generated Tests:")
    for t in res["generated_test_cases"]:
        print(f"  [{t['test_id']}] {t['assertion']}")

if __name__ == "__main__":
    main()
