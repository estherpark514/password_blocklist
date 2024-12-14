# Password Behavior Analysis

## Overview

This web application is designed to facilitate research on password behavior analysis:

**Authors**: Esther Park, Yuqi Hu, Sena Sahin, and Frank Li

The application consists of a simple signup page that collects passwords from participants to analyze their behavior when presented with varying password blocklists. The goal of this research is to evaluate how users interact with and respond to different password blocklists during the login process.

## Purpose

The primary objective of the research is to understand user behavior when confronted with password blocklists. The following blocklists were used in the study:

- **Blocklist #1**: Not currently available
- **Blocklist #2**: Not currently available
- **Blocklist #3**: Not currently available
- **Blocklist #4**: Not currently available

The study examines how these blocklists affect user behavior across both desktop and mobile experiences.

## Data Collection

The application collects various types of user interaction data:

### Login Information
- **Time Taken**: The duration spent entering the password.
- **Password Strength**: The strength of the password, assessed based on standard password metrics.
- **Success or Failure**: The outcome of the login attempt.

### Behavioral Data
- **Password Edits**: Tracks whether users delete or edit their password while typing.

## Technology Stack

### Frontend
- **Django REST Framework**: Used for collecting user data through a simple and functional interface.

### Backend
- **Django REST Framework**: Powers the backend to process, analyze, and store collected data.

### Admin Panel
- **Django Admin Panel**: Provides an interface to analyze and visualize password behavior and changes.

## Usage

This web app is designed to collect data for research purposes only and complies with ethical standards for data collection and privacy.

