"""
FAIR (Factor Analysis of Information Risk) Quantitative Simulation Engine
Performs Monte Carlo simulations comparing qualitative 5x5 matrix risk scores against
empirically grounded quantitative loss distributions (Annualized Loss Expectancy - ALE).
"""
import random
import math

def sample_pert(low: float, likely: float, high: float, gamma: float = 4.0) -> float:
    """
    Sample from a Beta-PERT distribution, standard in FAIR quantitative risk analysis.
    """
    if low >= high:
        return low
    mu = (low + gamma * likely + high) / (gamma + 2.0)
    # Estimate standard deviation
    sigma = (high - low) / (gamma + 2.0)
    if sigma <= 0:
        return likely
    
    alpha = ((mu - low) / (high - low)) * (((mu - low) * (high - mu) / (sigma ** 2)) - 1.0)
    beta = alpha * (high - mu) / (mu - low)
    
    if alpha <= 0 or beta <= 0:
        return likely

    # Python's random.betavariate operates on [0, 1]
    val = random.betavariate(alpha, beta)
    return low + val * (high - low)

def run_fair_monte_carlo(
    iterations: int = 10000,
    tef_low: float = 2.0,
    tef_likely: float = 12.0,
    tef_high: float = 35.0,
    control_strength: float = 0.75, # 0.0 (no control) to 0.95 (elite defense)
    loss_low: float = 25000.0,
    loss_likely: float = 120000.0,
    loss_high: float = 750000.0
):
    """
    Executes a 10,000 iteration FAIR Monte Carlo simulation.
    Calculates Annualized Loss Expectancy (ALE), 10th, 50th, 90th percentile (VaR).
    """
    random.seed(42) # Reproducible baseline
    annual_losses = []

    # Vulnerability is the probability that threat action penetrates given control strength
    vulnerability_base = 1.0 - control_strength

    for _ in range(iterations):
        # Sample Threat Event Frequency (attempts per year)
        threat_events = max(0, int(round(sample_pert(tef_low, tef_likely, tef_high))))
        
        # Determine actual loss events
        loss_events_count = 0
        for _ in range(threat_events):
            if random.random() < vulnerability_base:
                loss_events_count += 1
        
        # Calculate aggregate financial loss for this simulated year
        year_loss = 0.0
        for _ in range(loss_events_count):
            event_loss = sample_pert(loss_low, loss_likely, loss_high)
            year_loss += event_loss
        
        annual_losses.append(year_loss)

    annual_losses.sort()

    idx_10 = int(iterations * 0.10)
    idx_50 = int(iterations * 0.50)
    idx_90 = int(iterations * 0.90)
    idx_95 = int(iterations * 0.95)

    mean_ale = sum(annual_losses) / iterations

    # Histogram distribution bins (10 buckets)
    max_val = max(annual_losses) if annual_losses else 1.0
    bucket_size = max_val / 10 if max_val > 0 else 1.0
    bins = [{"min": round(i * bucket_size), "max": round((i + 1) * bucket_size), "count": 0} for i in range(10)]
    for loss in annual_losses:
        b_idx = min(9, int(loss / bucket_size)) if bucket_size > 0 else 0
        bins[b_idx]["count"] += 1

    return {
        "iterations": iterations,
        "control_strength_pct": round(control_strength * 100),
        "mean_ale": round(mean_ale, 2),
        "percentile_10": round(annual_losses[idx_10], 2),
        "median_50": round(annual_losses[idx_50], 2),
        "percentile_90_var": round(annual_losses[idx_90], 2),
        "percentile_95_var": round(annual_losses[idx_95], 2),
        "max_simulated_loss": round(annual_losses[-1], 2),
        "histogram_bins": bins,
        "academic_comparison": {
            "qualitative_grade": "High Risk (Likelihood 4 x Impact 5 = 20)",
            "fair_quantification": f"Expected loss (Mean ALE): ${mean_ale:,.0f}/year with 90% VaR of ${annual_losses[idx_90]:,.0f}.",
            "decision_value": "Eliminates ordinal scale ambiguity ('High vs Medium') and allows CFO/CISO cost-benefit analysis for control investments."
        }
    }

if __name__ == "__main__":
    result = run_fair_monte_carlo()
    print("FAIR Monte Carlo Simulation completed successfully:")
    print(f"Mean ALE: ${result['mean_ale']:,.2f}")
    print(f"90% VaR:  ${result['percentile_90_var']:,.2f}")
