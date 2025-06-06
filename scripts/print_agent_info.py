#!/usr/bin/env python3
"""Utility script to display basic agent information."""
import argparse
from pathlib import Path

from gaia_qao.agent import load_agent_profile


def print_active_quantum_reporting_info() -> None:
    """Print information about the Active Quantum Reporting Framework."""
    print("Active Quantum Reporting Framework:")
    print("  - Quantum Logger: Captures and logs all quantum operations")
    print("  - Quantum Analyzer: Analyzes quantum operation logs for performance and anomalies")
    print("  - Quantum Reporter: Generates reports based on analyzed data")
    print("  - Quantum Dashboard: Provides a user interface for monitoring and managing quantum operations")


def print_gaia_qao_cfd_automation_info() -> None:
    """Print information about the GAIA-QAO CFD Automation Script."""
    print("GAIA-QAO CFD Automation Script:")
    print("  - Automatic Validation: Checks system requirements and case structure before execution")
    print("  - Error Handling: Robust error detection and management with detailed logs")
    print("  - Scalability: Supports parallel execution with automatic core detection")
    print("  - Traceability: Comprehensive logging system with timestamps and performance metrics")
    print("  - Backup: Automatically backs up previous results before new runs")
    print("  - Reporting: Generates executive summary reports post-simulation")


def main() -> None:
    parser = argparse.ArgumentParser(description="Display agent profile info")
    parser.add_argument(
        "profile",
        type=Path,
        default=Path("Q-AI/agent_profile_sustainability.yaml"),
        nargs="?",
        help="Path to agent profile YAML",
    )
    args = parser.parse_args()

    profile = load_agent_profile(args.profile)
    print(f"Agent ID: {profile.agent_id}")
    print(f"Agent Name: {profile.agent_name}")
    print(f"Description: {profile.description}")

    print_active_quantum_reporting_info()
    print_gaia_qao_cfd_automation_info()


if __name__ == "__main__":
    main()
