#!/usr/bin/env python
import pprint
import argparse

from compliance_checker.runner import ComplianceChecker, ComplianceCheckerCheckSuite

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset_location', nargs=1, help= "Defines the location of the dataset to be checked.")
    parser.add_argument('--test', '-t', '--test=', '-t=', help= "Select the Checks you want to perform.  Either all (default), cf, ioos, or acdd.", nargs='+', default=[], choices=ComplianceCheckerCheckSuite.checkers.keys())
    parser.add_argument('--criteria', '-c', help="Define the criteria for the checks.  Either Strict, Normal, or Lenient.  Defaults to Normal.", nargs='?', default='normal', choices = ['lenient', 'normal', 'strict'])
    parser.add_argument('--verbose' , '-v', help="Increase Output Verbosity", action="count")

    args = parser.parse_args()

    print "Running Compliance Checker on the dataset from: %s" % args.dataset_location[0]

    ComplianceChecker.run_checker(args.dataset_location[0],
                                  args.test,
                                  args.verbose,
                                  args.criteria)

if __name__ == "__main__":
    main()
