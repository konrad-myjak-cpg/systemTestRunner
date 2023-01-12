import subprocess
import config
import time
import os

testResultsPath = './data/testResults.csv'
testListPath = './data/testsList.txt'

class AdbController():
    def setReversePortRedirection(self, port):
        os.system(f"adb reverse tcp:{port} tcp:{port}")

    def removeApp(self, appBundleID):
        os.system(f"adb uninstall {appBundleID}")

    def installApp(self, apkPath):
        os.system(f"adb install {apkPath}")

    def startActivity(self, appID, testName):
        os.system(f"adb shell am start  -n {appID}/com.crimsonpine.crimsonnative.CrimsonUnityPlayerActivity --es test_key {testName}")

    def getTestsList(self):
        file = open(testListPath, 'r')
        return file.readlines()

    def isActivityRunning(self, app_bundleID):
        result = os.system(f"adb shell pidof {app_bundleID}")
        return result == 0

    def runTestLoop(self):
        self.removeApp(config.app_bundleID)
        self.installApp(config.apk_path)
        tests = self.getTestsList()
        for test in tests:
            print(test)
            self.startActivity(config.app_bundleID, test)
            while self.isActivityRunning(config.app_bundleID):
                time.sleep(0.5)



