---
title: "Ashby"
---
Ashby connects an Agent to recruiting records. Depending on the key permissions, it can search candidates and applications, retrieve job and report information, look up users and referral forms, and create candidate notes or referrals.

## Set up access

An administrator adds Ashby from **Spaces → Tools → Add Tools** and supplies an Ashby API key. In Ashby Admin, create a key for the intended workspace. The source setup requires Candidates read/write for candidate search, application details, feedback, notes, and referrals; Jobs read for job listings; Reports read for report data; Organization read for user lookup; and Hiring Process read for referral forms. Grant confidential-job or private-field access only when those records are intentionally in scope.

Add the configured tool to the relevant Agent and confirm the key belongs to the correct Ashby organization. Begin with a candidate search or job listing. A valid key may still lack permission for the requested object, so check the specific permission area when results are missing. Review any candidate note or referral before creating it.

## Available operations

Available tools include candidate search, candidate notes, application details and interview feedback, referral form retrieval, referral creation, job listing, synchronous reports, and user search: `Search Candidates`, `List Candidate Notes`, `Create Candidate Note`, `Get Application Details`, `Get Application Feedback`, `Get Referral Form`, `Create Referral`, `List Jobs`, `Run Synchronous Report`, and `Search Users`. Grant the candidate write permission only for notes/referrals; read permissions on Jobs, Reports, Organization, and Hiring Process support the corresponding lookups.
