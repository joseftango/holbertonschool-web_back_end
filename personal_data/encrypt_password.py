#!/usr/bin/env python3
"""Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Performs a password hashing using the `bcrypt` package
    Args:
        password: string type to be hashed
    Returns:
        a salted, hashed password, which is a byte string.
    """
    p = password.encode()
    return bcrypt.hashpw(p, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """is_valid function"""
    return bcrypt.checkpw(password.encode(), hashed_password)
