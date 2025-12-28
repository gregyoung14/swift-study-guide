---
id: 1043
---
# macOS Development

## Overview

macOS development encompasses creating applications for Apple's desktop operating system, powering Mac computers. Swift is the primary language for modern macOS development, offering powerful frameworks and tools for building professional desktop applications. This guide covers the essential concepts, frameworks, and best practices for macOS app development.

## Table of Contents

- [macOS Platform Overview](#macos-platform-overview)
- [AppKit Framework](#appkit-framework)
- [Application Architecture](#application-architecture)
- [User Interface Design](#user-interface-design)
- [Data Persistence](#data-persistence)
- [System Integration](#system-integration)
- [Security and Sandboxing](#security-and-sandboxing)
- [Distribution and Deployment](#distribution-and-deployment)
- [Performance Optimization](#performance-optimization)

## macOS Platform Overview

### Platform Characteristics

```swift
// macOS platform specifications
struct MacOSPlatform {
    static let currentVersion = "macOS Sonoma (14.0+)"
    static let supportedArchitectures = ["Intel x64", "Apple Silicon"]
    static let minimumRequirements = HardwareRequirements()

    struct HardwareRequirements {
        let processor = "Intel Core 2 Duo or Apple Silicon"
        let memory = "4 GB RAM (8 GB recommended)"
        let storage = "25 GB available space"
        let display = "1280 x 800 resolution"
    }
}
```

### Development Environment

```swift
// macOS development ecosystem
struct DevelopmentEnvironment {
    let primaryLanguage = "Swift"
    let uiFramework = "AppKit"
    let declarativeUI = "SwiftUI (macOS 10.15+)"
    let ide = "Xcode"
    let deploymentTarget = "macOS 11.0+ (recommended)"

    let supportedFrameworks = [
        "AppKit": "Native UI components",
        "Foundation": "Core functionality",
        "CoreData": "Data persistence",
        "CoreGraphics": "2D graphics",
        "CoreAnimation": "Animations",
        "CoreImage": "Image processing"
    ]
}
```

### App Categories

```swift
// Types of macOS applications
enum MacAppCategory {
    case documentBased        // Text editors, IDEs, design tools
    case utility             // Calculators, converters, system monitors
    case media               // Players, editors, streaming apps
    case productivity        // Email, calendars, project management
    case creative            // Photo editors, video editors, DAWs
    case development         // IDEs, debuggers, version control
    case games               // 2D/3D games, casual gaming
    case system              // Extensions, background services
}
```

## AppKit Framework

### Window and View Management

```swift
// AppKit window management
import AppKit

class MainWindowController: NSWindowController {
    override func windowDidLoad() {
        super.windowDidLoad()

        // Configure window
        window?.title = "My macOS App"
        window?.styleMask = [.titled, .closable, .miniaturizable, .resizable]
        window?.setContentSize(NSSize(width: 800, height: 600))

        // Set minimum size
        window?.minSize = NSSize(width: 400, height: 300)

        // Center on screen
        window?.center()
    }
}

// View controller with AppKit
class ContentViewController: NSViewController {

    private var textField: NSTextField!
    private var button: NSButton!

    override func loadView() {
        self.view = NSView(frame: NSRect(x: 0, y: 0, width: 400, height: 300))
        setupUI()
    }

    private func setupUI() {
        // Create text field
        textField = NSTextField(frame: NSRect(x: 20, y: 250, width: 360, height: 24))
        textField.placeholderString = "Enter your name"
        view.addSubview(textField)

        // Create button
        button = NSButton(frame: NSRect(x: 20, y: 200, width: 100, height: 32))
        button.title = "Greet"
        button.bezelStyle = .rounded
        button.target = self
        button.action = #selector(greetUser)
        view.addSubview(button)
    }

    @objc private func greetUser() {
        let name = textField.stringValue
        if name.isEmpty {
            showAlert(message: "Please enter your name")
        } else {
            showAlert(message: "Hello, \(name)!")
        }
    }

    private func showAlert(message: String) {
        let alert = NSAlert()
        alert.messageText = "Greeting"
        alert.informativeText = message
        alert.alertStyle = .informational
        alert.addButton(withTitle: "OK")
        alert.runModal()
    }
}
```

### Menu Management

```swift
// Application menu setup
class AppDelegate: NSObject, NSApplicationDelegate {

    func applicationDidFinishLaunching(_ notification: Notification) {
        setupMainMenu()
    }

    private func setupMainMenu() {
        let mainMenu = NSMenu()

        // Application menu
        let appMenu = NSMenu()
        appMenu.addItem(withTitle: "About MyApp",
                       action: #selector(showAbout),
                       keyEquivalent: "")
        appMenu.addItem(NSMenuItem.separator())
        appMenu.addItem(withTitle: "Quit MyApp",
                       action: #selector(NSApplication.terminate(_:)),
                       keyEquivalent: "q")

        let appMenuItem = mainMenu.addItem(withTitle: "MyApp", action: nil, keyEquivalent: "")
        appMenuItem.submenu = appMenu

        // File menu
        let fileMenu = NSMenu(title: "File")
        fileMenu.addItem(withTitle: "New",
                        action: #selector(newDocument),
                        keyEquivalent: "n")
        fileMenu.addItem(withTitle: "Open...",
                        action: #selector(openDocument),
                        keyEquivalent: "o")
        fileMenu.addItem(NSMenuItem.separator())
        fileMenu.addItem(withTitle: "Save",
                        action: #selector(saveDocument),
                        keyEquivalent: "s")

        let fileMenuItem = mainMenu.addItem(withTitle: "File", action: nil, keyEquivalent: "")
        fileMenuItem.submenu = fileMenu

        // Edit menu (standard)
        let editMenuItem = mainMenu.addItem(withTitle: "Edit", action: nil, keyEquivalent: "")
        editMenuItem.submenu = NSMenu(title: "Edit")

        NSApplication.shared.mainMenu = mainMenu
    }

    @objc private func showAbout() {
        let about = NSAlert()
        about.messageText = "About MyApp"
        about.informativeText = "Version 1.0"
        about.runModal()
    }

    // Menu action implementations
    @objc private func newDocument() { /* Implementation */ }
    @objc private func openDocument() { /* Implementation */ }
    @objc private func saveDocument() { /* Implementation */ }
}
```

### Document-Based Applications

```swift
// Document-based app architecture
class Document: NSDocument {

    var content: String = ""

    override func makeWindowControllers() {
        let storyboard = NSStoryboard(name: "Main", bundle: nil)
        let windowController = storyboard.instantiateController(
            withIdentifier: "Document Window Controller"
        ) as! NSWindowController

        addWindowController(windowController)
    }

    override func data(ofType typeName: String) throws -> Data {
        guard let data = content.data(using: .utf8) else {
            throw NSError(domain: "DocumentError", code: 1, userInfo: nil)
        }
        return data
    }

    override func read(from data: Data, ofType typeName: String) throws {
        guard let string = String(data: data, using: .utf8) else {
            throw NSError(domain: "DocumentError", code: 2, userInfo: nil)
        }
        content = string
    }

    override class var autosavesInPlace: Bool {
        return true
    }
}

// Document controller
class DocumentController: NSDocumentController {

    override func newDocument(_ sender: Any?) {
        do {
            try openUntitledDocumentAndDisplay(true)
        } catch {
            presentError(error)
        }
    }

    override func openDocument(_ sender: Any?) {
        let panel = NSOpenPanel()
        panel.allowedFileTypes = ["txt"]
        panel.begin { response in
            if response == .OK, let url = panel.url {
                do {
                    try self.openDocument(withContentsOf: url, display: true)
                } catch {
                    self.presentError(error)
                }
            }
        }
    }
}
```

## Application Architecture

### NSApplication and App Delegate

```swift
// Application lifecycle management
import AppKit

@main
class AppDelegate: NSObject, NSApplicationDelegate {

    var mainWindowController: MainWindowController?

    func applicationDidFinishLaunching(_ notification: Notification) {
        // Initialize app-wide services
        setupServices()
        setupUserInterface()

        // Show main window
        mainWindowController = MainWindowController()
        mainWindowController?.showWindow(self)
    }

    func applicationWillTerminate(_ notification: Notification) {
        // Cleanup resources
        saveApplicationState()
        shutdownServices()
    }

    func applicationShouldHandleReopen(_ sender: NSApplication, hasVisibleWindows flag: Bool) -> Bool {
        if !flag {
            mainWindowController?.showWindow(self)
        }
        return true
    }

    // Dock icon click handling
    func applicationShouldOpenUntitledFile(_ sender: NSApplication) -> Bool {
        // Create new untitled document
        return true
    }

    private func setupServices() {
        // Initialize core services
        UserDefaults.standard.register(defaults: [
            "DefaultFontSize": 12,
            "ShowLineNumbers": true
        ])
    }

    private func setupUserInterface() {
        // Configure UI appearance
        NSApplication.shared.appearance = NSAppearance(named: .aqua)
    }

    private func saveApplicationState() {
        // Save window positions, preferences, etc.
        mainWindowController?.window?.saveFrame(usingName: "MainWindow")
    }

    private func shutdownServices() {
        // Clean shutdown of services
        NotificationCenter.default.removeObserver(self)
    }
}
```

### Responder Chain

```swift
// Event handling through responder chain
class CustomView: NSView {

    override func mouseDown(with event: NSEvent) {
        let location = convert(event.locationInWindow, from: nil)

        if bounds.contains(location) {
            // Handle click in this view
            print("View clicked at \(location)")
        } else {
            // Pass to next responder
            super.mouseDown(with: event)
        }
    }

    override func keyDown(with event: NSEvent) {
        switch event.characters {
        case " ":
            // Handle space key
            togglePlayback()
        case "\r":
            // Handle return key
            performAction()
        default:
            // Pass to next responder
            super.keyDown(with: event)
        }
    }

    private func togglePlayback() {
        // Toggle playback logic
    }

    private func performAction() {
        // Perform primary action
    }
}

// Window controller responder
class MainWindowController: NSWindowController {

    override func keyDown(with event: NSEvent) {
        // Handle global shortcuts
        if event.modifierFlags.contains(.command) {
            switch event.characters {
            case "n":
                createNewDocument()
            case "o":
                openDocument()
            case "s":
                saveDocument()
            default:
                super.keyDown(with: event)
            }
        } else {
            super.keyDown(with: event)
        }
    }

    private func createNewDocument() { /* Implementation */ }
    private func openDocument() { /* Implementation */ }
    private func saveDocument() { /* Implementation */ }
}
```

## User Interface Design

### Auto Layout Constraints

```swift
// Programmatic Auto Layout
class LayoutViewController: NSViewController {

    private var usernameField: NSTextField!
    private var passwordField: NSTextField!
    private var loginButton: NSButton!

    override func loadView() {
        view = NSView()
        setupViews()
        setupConstraints()
    }

    private func setupViews() {
        usernameField = NSTextField()
        usernameField.placeholderString = "Username"
        usernameField.translatesAutoresizingMaskIntoConstraints = false

        passwordField = NSSecureTextField()
        passwordField.placeholderString = "Password"
        passwordField.translatesAutoresizingMaskIntoConstraints = false

        loginButton = NSButton(title: "Login", target: self, action: #selector(login))
        loginButton.translatesAutoresizingMaskIntoConstraints = false

        view.addSubview(usernameField)
        view.addSubview(passwordField)
        view.addSubview(loginButton)
    }

    private func setupConstraints() {
        NSLayoutConstraint.activate([
            // Username field
            usernameField.topAnchor.constraint(equalTo: view.topAnchor, constant: 20),
            usernameField.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20),
            usernameField.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20),
            usernameField.heightAnchor.constraint(equalToConstant: 24),

            // Password field
            passwordField.topAnchor.constraint(equalTo: usernameField.bottomAnchor, constant: 12),
            passwordField.leadingAnchor.constraint(equalTo: usernameField.leadingAnchor),
            passwordField.trailingAnchor.constraint(equalTo: usernameField.trailingAnchor),
            passwordField.heightAnchor.constraint(equalTo: usernameField.heightAnchor),

            // Login button
            loginButton.topAnchor.constraint(equalTo: passwordField.bottomAnchor, constant: 20),
            loginButton.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            loginButton.widthAnchor.constraint(equalToConstant: 100),
            loginButton.heightAnchor.constraint(equalToConstant: 32),

            // Container constraints
            view.widthAnchor.constraint(greaterThanOrEqualToConstant: 300),
            view.heightAnchor.constraint(greaterThanOrEqualToConstant: 150)
        ])
    }

    @objc private func login() {
        // Login logic
    }
}
```

### SwiftUI for macOS

```swift
// SwiftUI on macOS
import SwiftUI

@main
struct MacApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
        .commands {
            // Add menu commands
            CommandGroup(replacing: .newItem) {
                Button("New Document") {
                    // Create new document
                }
                .keyboardShortcut("n")
            }

            CommandGroup(replacing: .saveItem) {
                Button("Save") {
                    // Save document
                }
                .keyboardShortcut("s")
            }
        }
    }
}

struct ContentView: View {
    @State private var username = ""
    @State private var password = ""
    @State private var isLoggedIn = false

    var body: some View {
        if isLoggedIn {
            MainView()
        } else {
            LoginView(username: $username, password: $password, isLoggedIn: $isLoggedIn)
        }
    }
}

struct LoginView: View {
    @Binding var username: String
    @Binding var password: String
    @Binding var isLoggedIn: Bool

    var body: some View {
        VStack(spacing: 20) {
            Text("Login to macOS App")
                .font(.title)

            TextField("Username", text: $username)
                .frame(width: 200)

            SecureField("Password", text: $password)
                .frame(width: 200)

            Button("Login") {
                authenticate()
            }
            .buttonStyle(.borderedProminent)
        }
        .padding(40)
        .frame(minWidth: 300, minHeight: 200)
    }

    private func authenticate() {
        // Authentication logic
        if !username.isEmpty && !password.isEmpty {
            isLoggedIn = true
        }
    }
}

struct MainView: View {
    var body: some View {
        Text("Welcome to the app!")
            .font(.largeTitle)
    }
}
```

### Interface Builder Integration

```swift
// Storyboard and XIB integration
class StoryboardViewController: NSViewController {

    // Outlets
    @IBOutlet private weak var nameLabel: NSTextField!
    @IBOutlet private weak var emailLabel: NSTextField!
    @IBOutlet private weak var saveButton: NSButton!

    // Actions
    @IBAction private func saveButtonClicked(_ sender: NSButton) {
        saveUserData()
    }

    @IBAction private func cancelButtonClicked(_ sender: NSButton) {
        dismissViewController()
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }

    private func setupUI() {
        // Additional programmatic setup
        nameLabel.stringValue = "John Doe"
        emailLabel.stringValue = "john@example.com"
    }

    private func saveUserData() {
        let user = User(
            name: nameLabel.stringValue,
            email: emailLabel.stringValue
        )
        // Save user data
        dismissViewController()
    }

    private func dismissViewController() {
        if let window = view.window?.sheetParent {
            window.endSheet(window)
        }
    }
}
```

## Data Persistence

### UserDefaults for Preferences

```swift
// Application preferences
class AppPreferences {
    private let defaults = UserDefaults.standard

    // Keys
    private enum Keys {
        static let theme = "theme"
        static let fontSize = "fontSize"
        static let showToolbar = "showToolbar"
        static let recentFiles = "recentFiles"
    }

    // Computed properties
    var theme: Theme {
        get {
            let rawValue = defaults.string(forKey: Keys.theme) ?? "system"
            return Theme(rawValue: rawValue) ?? .system
        }
        set {
            defaults.set(newValue.rawValue, forKey: Keys.theme)
        }
    }

    var fontSize: Double {
        get { defaults.double(forKey: Keys.fontSize) }
        set { defaults.set(newValue, forKey: Keys.fontSize) }
    }

    var showToolbar: Bool {
        get { defaults.bool(forKey: Keys.showToolbar) }
        set { defaults.set(newValue, forKey: Keys.showToolbar) }
    }

    var recentFiles: [URL] {
        get {
            let urls = defaults.array(forKey: Keys.recentFiles) as? [String] ?? []
            return urls.compactMap { URL(string: $0) }
        }
        set {
            let urls = newValue.map { $0.absoluteString }
            defaults.set(urls, forKey: Keys.recentFiles)
        }
    }

    // Complex objects with JSON
    func saveWindowState(_ state: WindowState) {
        if let data = try? JSONEncoder().encode(state) {
            defaults.set(data, forKey: "windowState")
        }
    }

    func loadWindowState() -> WindowState? {
        guard let data = defaults.data(forKey: "windowState") else { return nil }
        return try? JSONDecoder().decode(WindowState.self, from: data)
    }
}

enum Theme: String {
    case light, dark, system
}

struct WindowState: Codable {
    let frame: NSRect
    let isVisible: Bool
    let toolbarVisible: Bool
}
```

### Core Data for Complex Data

```swift
// Core Data setup for macOS
class CoreDataManager {
    static let shared = CoreDataManager()

    let persistentContainer: NSPersistentContainer

    private init() {
        persistentContainer = NSPersistentContainer(name: "MacAppModel")
        persistentContainer.loadPersistentStores { description, error in
            if let error = error {
                fatalError("Unable to load persistent stores: \(error.localizedDescription)")
            }
        }

        // Enable automatic merging of changes from parent context
        persistentContainer.viewContext.automaticallyMergesChangesFromParent = true
    }

    var context: NSManagedObjectContext {
        persistentContainer.viewContext
    }

    func saveContext() {
        if context.hasChanges {
            do {
                try context.save()
            } catch {
                let nserror = error as NSError
                fatalError("Unresolved error \(nserror), \(nserror.userInfo)")
            }
        }
    }
}

// Document model
@objc(Document)
class Document: NSManagedObject {
    @NSManaged var id: UUID
    @NSManaged var title: String
    @NSManaged var content: String
    @NSManaged var createdAt: Date
    @NSManaged var modifiedAt: Date
    @NSManaged var tags: NSSet?

    var tagArray: [Tag] {
        let set = tags as? Set<Tag> ?? []
        return Array(set).sorted { $0.name < $1.name }
    }
}

// Document operations
class DocumentManager {
    private let coreDataManager = CoreDataManager.shared

    func createDocument(title: String, content: String = "") throws -> Document {
        let document = Document(context: coreDataManager.context)
        document.id = UUID()
        document.title = title
        document.content = content
        document.createdAt = Date()
        document.modifiedAt = Date()

        try coreDataManager.context.save()
        return document
    }

    func fetchDocuments() throws -> [Document] {
        let request = NSFetchRequest<Document>(entityName: "Document")
        request.sortDescriptors = [NSSortDescriptor(key: "modifiedAt", ascending: false)]
        return try coreDataManager.context.fetch(request)
    }

    func updateDocument(_ document: Document, title: String? = nil, content: String? = nil) throws {
        if let title = title {
            document.title = title
        }
        if let content = content {
            document.content = content
        }
        document.modifiedAt = Date()
        try coreDataManager.context.save()
    }

    func deleteDocument(_ document: Document) throws {
        coreDataManager.context.delete(document)
        try coreDataManager.context.save()
    }
}
```

### File System Operations

```swift
// File system operations for macOS
class FileManager {
    static let shared = FileManager()

    private let fileManager = Foundation.FileManager.default
    private let documentsDirectory: URL

    private init() {
        documentsDirectory = fileManager.urls(
            for: .documentDirectory,
            in: .userDomainMask
        )[0]
    }

    // Save data to file
    func saveData(_ data: Data, filename: String, subdirectory: String? = nil) throws {
        var fileURL = documentsDirectory

        if let subdirectory = subdirectory {
            fileURL.appendPathComponent(subdirectory)
            try createDirectoryIfNeeded(at: fileURL)
        }

        fileURL.appendPathComponent(filename)
        try data.write(to: fileURL)
    }

    // Load data from file
    func loadData(filename: String, subdirectory: String? = nil) throws -> Data {
        var fileURL = documentsDirectory

        if let subdirectory = subdirectory {
            fileURL.appendPathComponent(subdirectory)
        }

        fileURL.appendPathComponent(filename)
        return try Data(contentsOf: fileURL)
    }

    // Create directory if needed
    private func createDirectoryIfNeeded(at url: URL) throws {
        if !fileManager.fileExists(atPath: url.path) {
            try fileManager.createDirectory(
                at: url,
                withIntermediateDirectories: true
            )
        }
    }

    // List files in directory
    func listFiles(in subdirectory: String? = nil) throws -> [URL] {
        var directoryURL = documentsDirectory

        if let subdirectory = subdirectory {
            directoryURL.appendPathComponent(subdirectory)
        }

        return try fileManager.contentsOfDirectory(
            at: directoryURL,
            includingPropertiesForKeys: nil
        )
    }

    // File operations with security scoping
    func readFileWithSecurityScope(url: URL) throws -> Data {
        guard url.startAccessingSecurityScopedResource() else {
            throw FileError.accessDenied
        }

        defer {
            url.stopAccessingSecurityScopedResource()
        }

        return try Data(contentsOf: url)
    }
}

enum FileError: Error {
    case accessDenied
    case fileNotFound
    case permissionDenied
}
```

## System Integration

### Notifications

```swift
// User notifications
import UserNotifications

class NotificationManager {
    static let shared = NotificationManager()

    private let center = UNUserNotificationCenter.current()

    func requestPermission() async throws -> Bool {
        let options: UNAuthorizationOptions = [.alert, .sound, .badge]
        return try await center.requestAuthorization(options: options)
    }

    func scheduleNotification(title: String, body: String, delay: TimeInterval = 5) {
        let content = UNMutableNotificationContent()
        content.title = title
        content.body = body
        content.sound = .default

        let trigger = UNTimeIntervalNotificationTrigger(timeInterval: delay, repeats: false)
        let request = UNNotificationRequest(identifier: UUID().uuidString, content: content, trigger: trigger)

        center.add(request) { error in
            if let error = error {
                print("Error scheduling notification: \(error)")
            }
        }
    }

    func showBannerNotification(title: String, body: String) {
        let content = UNMutableNotificationContent()
        content.title = title
        content.body = body

        let request = UNNotificationRequest(identifier: UUID().uuidString, content: content, trigger: nil)

        center.add(request) { error in
            if let error = error {
                print("Error showing notification: \(error)")
            }
        }
    }
}
```

### System Services

```swift
// Integration with system services
class SystemIntegrationManager {

    // Open URL in default browser
    func openURL(_ url: URL) {
        NSWorkspace.shared.open(url)
    }

    // Open file with default application
    func openFile(_ url: URL) {
        NSWorkspace.shared.open(url)
    }

    // Show file in Finder
    func showInFinder(_ url: URL) {
        NSWorkspace.shared.activateFileViewerSelecting([url])
    }

    // Get system information
    func getSystemInfo() -> SystemInfo {
        let processInfo = ProcessInfo.processInfo

        return SystemInfo(
            processorCount: processInfo.processorCount,
            activeProcessorCount: processInfo.activeProcessorCount,
            physicalMemory: processInfo.physicalMemory,
            systemVersion: getSystemVersion()
        )
    }

    private func getSystemVersion() -> String {
        let version = ProcessInfo.processInfo.operatingSystemVersion
        return "\(version.majorVersion).\(version.minorVersion).\(version.patchVersion)"
    }

    // Monitor system events
    func startMonitoringSystemEvents() {
        let workspace = NSWorkspace.shared

        workspace.notificationCenter.addObserver(
            self,
            selector: #selector(systemWillSleep),
            name: NSWorkspace.willSleepNotification,
            object: nil
        )

        workspace.notificationCenter.addObserver(
            self,
            selector: #selector(systemDidWake),
            name: NSWorkspace.didWakeNotification,
            object: nil
        )
    }

    @objc private func systemWillSleep() {
        // Save state before sleep
        print("System going to sleep")
    }

    @objc private func systemDidWake() {
        // Restore state after wake
        print("System woke up")
    }
}

struct SystemInfo {
    let processorCount: Int
    let activeProcessorCount: Int
    let physicalMemory: UInt64
    let systemVersion: String
}
```

### Pasteboard Operations

```swift
// Clipboard operations
class ClipboardManager {
    private let pasteboard = NSPasteboard.general

    // Copy text to clipboard
    func copyText(_ text: String) {
        pasteboard.clearContents()
        pasteboard.setString(text, forType: .string)
    }

    // Copy multiple items
    func copyMultipleItems(items: [PasteboardItem]) {
        pasteboard.clearContents()

        let pasteboardItems = items.map { item -> NSPasteboardItem in
            let pasteboardItem = NSPasteboardItem()
            pasteboardItem.setString(item.text, forType: .string)

            if let url = item.url {
                pasteboardItem.setString(url.absoluteString, forType: .URL)
            }

            return pasteboardItem
        }

        pasteboard.writeObjects(pasteboardItems)
    }

    // Read text from clipboard
    func getText() -> String? {
        return pasteboard.string(forType: .string)
    }

    // Read multiple items
    func getMultipleItems() -> [PasteboardItem] {
        guard let items = pasteboard.pasteboardItems else { return [] }

        return items.compactMap { item in
            guard let text = item.string(forType: .string) else { return nil }

            var url: URL? = nil
            if let urlString = item.string(forType: .URL) {
                url = URL(string: urlString)
            }

            return PasteboardItem(text: text, url: url)
        }
    }

    // Monitor clipboard changes
    func startMonitoringChanges(callback: @escaping () -> Void) {
        let timer = Timer.scheduledTimer(withTimeInterval: 1.0, repeats: true) { _ in
            // Check for changes (simplified)
            callback()
        }
        RunLoop.current.add(timer, forMode: .common)
    }
}

struct PasteboardItem {
    let text: String
    let url: URL?
}
```

## Security and Sandboxing

### App Sandbox

```swift
// App Sandbox entitlements (entitlements file)
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>com.apple.security.app-sandbox</key>
    <true/>
    <key>com.apple.security.files.user-selected.read-write</key>
    <true/>
    <key>com.apple.security.files.downloads.read-write</key>
    <true/>
    <key>com.apple.security.network.client</key>
    <true/>
    <key>com.apple.security.network.server</key>
    <false/>
</dict>
</plist>

// Sandbox-aware file operations
class SandboxedFileManager {
    private let fileManager = Foundation.FileManager.default

    // Request access to user-selected file
    func requestAccessToFile(completion: @escaping (URL?) -> Void) {
        let panel = NSOpenPanel()
        panel.canChooseFiles = true
        panel.canChooseDirectories = false
        panel.allowsMultipleSelection = false

        panel.begin { response in
            if response == .OK {
                completion(panel.url)
            } else {
                completion(nil)
            }
        }
    }

    // Read file with security-scoped access
    func readFileWithAccess(url: URL) throws -> Data {
        guard url.startAccessingSecurityScopedResource() else {
            throw SecurityError.accessDenied
        }

        defer {
            url.stopAccessingSecurityScopedResource()
        }

        return try Data(contentsOf: url)
    }

    // Check sandbox restrictions
    func checkSandboxRestrictions() {
        // Check what resources are accessible
        let homeURL = fileManager.homeDirectoryForCurrentUser
        let documentsURL = fileManager.urls(for: .documentDirectory, in: .userDomainMask)[0]

        print("Can access home directory: \(fileManager.isReadableFile(atPath: homeURL.path))")
        print("Can access documents: \(fileManager.isReadableFile(atPath: documentsURL.path))")
    }
}

enum SecurityError: Error {
    case accessDenied
    case sandboxViolation
}
```

### Keychain Services

```swift
// Secure credential storage
import Security

class KeychainManager {
    private let serviceName = "com.example.MyMacApp"

    // Save password to keychain
    func savePassword(account: String, password: String) throws {
        let passwordData = password.data(using: .utf8)!

        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: serviceName,
            kSecAttrAccount as String: account,
            kSecValueData as String: passwordData
        ]

        // Delete existing item
        SecItemDelete(query as CFDictionary)

        // Add new item
        let status = SecItemAdd(query as CFDictionary, nil)
        guard status == errSecSuccess else {
            throw KeychainError.saveFailed(status)
        }
    }

    // Retrieve password from keychain
    func getPassword(account: String) throws -> String {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: serviceName,
            kSecAttrAccount as String: account,
            kSecReturnData as String: true,
            kSecMatchLimit as String: kSecMatchLimitOne
        ]

        var result: AnyObject?
        let status = SecItemCopyMatching(query as CFDictionary, &result)

        guard status == errSecSuccess,
              let passwordData = result as? Data,
              let password = String(data: passwordData, using: .utf8) else {
            throw KeychainError.retrieveFailed(status)
        }

        return password
    }

    // Delete password from keychain
    func deletePassword(account: String) throws {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: serviceName,
            kSecAttrAccount as String: account
        ]

        let status = SecItemDelete(query as CFDictionary)
        guard status == errSecSuccess || status == errSecItemNotFound else {
            throw KeychainError.deleteFailed(status)
        }
    }

    // Update password
    func updatePassword(account: String, newPassword: String) throws {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: serviceName,
            kSecAttrAccount as String: account
        ]

        let updateQuery: [String: Any] = [
            kSecValueData as String: newPassword.data(using: .utf8)!
        ]

        let status = SecItemUpdate(query as CFDictionary, updateQuery as CFDictionary)
        guard status == errSecSuccess else {
            throw KeychainError.updateFailed(status)
        }
    }
}

enum KeychainError: Error {
    case saveFailed(OSStatus)
    case retrieveFailed(OSStatus)
    case deleteFailed(OSStatus)
    case updateFailed(OSStatus)
}
```

## Distribution and Deployment

### App Store Connect

```swift
// App Store Connect submission process
struct AppStoreSubmission {
    let preparationSteps = [
        "Create App Store Connect record",
        "Configure app information and metadata",
        "Set up pricing and availability",
        "Prepare screenshots for different devices",
        "Write app description and keywords",
        "Configure in-app purchases if applicable"
    ]

    let buildSteps = [
        "Archive build in Xcode (Product → Archive)",
        "Validate archive for App Store",
        "Upload build to App Store Connect",
        "Wait for processing (usually 10-30 minutes)"
    ]

    let testingSteps = [
        "Set up TestFlight beta testing",
        "Invite internal testers",
        "Submit for external beta review if needed",
        "Gather feedback and fix issues",
        "Conduct regression testing"
    ]

    let releaseSteps = [
        "Submit app for App Store review",
        "Wait for review (typically 1-2 days)",
        "Address any review feedback",
        "Release app manually or automatically",
        "Monitor crash reports and user feedback"
    ]
}
```

### Code Signing and Notarization

```swift
// Code signing configuration
struct CodeSigningConfig {
    let developmentTeam = "YOUR_TEAM_ID"
    let bundleIdentifier = "com.example.MyMacApp"
    let provisioningProfile = "Mac App Store Distribution"

    // Xcode build settings
    let buildSettings = [
        "CODE_SIGN_IDENTITY": "Apple Distribution",
        "DEVELOPMENT_TEAM": developmentTeam,
        "PROVISIONING_PROFILE_SPECIFIER": provisioningProfile,
        "CODE_SIGN_STYLE": "Automatic"
    ]
}

// Notarization script (for non-App Store distribution)
class NotarizationManager {
    func notarizeApp(at appURL: URL) async throws {
        let zipURL = try await createZipArchive(of: appURL)
        let requestUUID = try await submitForNotarization(zipURL)
        try await waitForNotarization(requestUUID)
        try await stapleNotarization(to: appURL)
    }

    private func createZipArchive(of appURL: URL) async throws -> URL {
        let zipURL = appURL.deletingPathExtension().appendingPathExtension("zip")
        let process = Process()
        process.executableURL = URL(fileURLWithPath: "/usr/bin/ditto")
        process.arguments = ["-c", "-k", "--keepParent", appURL.path, zipURL.path]

        try await process.run()
        process.waitUntilExit()

        return zipURL
    }

    private func submitForNotarization(_ zipURL: URL) async throws -> String {
        let process = Process()
        process.executableURL = URL(fileURLWithPath: "/usr/bin/xcrun")
        process.arguments = [
            "notarytool", "submit",
            zipURL.path,
            "--apple-id", "your-apple-id@example.com",
            "--password", "app-specific-password",
            "--team-id", "YOUR_TEAM_ID"
        ]

        // Capture output for UUID
        let outputPipe = Pipe()
        process.standardOutput = outputPipe

        try await process.run()
        process.waitUntilExit()

        let outputData = outputPipe.fileHandleForReading.readDataToEndOfFile()
        let output = String(data: outputData, encoding: .utf8) ?? ""

        // Extract UUID from output (simplified)
        return extractSubmissionID(from: output)
    }

    private func waitForNotarization(_ requestUUID: String) async throws {
        // Poll for completion status
        try await Task.sleep(nanoseconds: 30_000_000_000) // 30 seconds
        // Check status and retry if needed
    }

    private func stapleNotarization(to appURL: URL) async throws {
        let process = Process()
        process.executableURL = URL(fileURLWithPath: "/usr/bin/xcrun")
        process.arguments = ["stapler", "staple", appURL.path]

        try await process.run()
        process.waitUntilExit()
    }

    private func extractSubmissionID(from output: String) -> String {
        // Parse submission ID from notarytool output
        return "placeholder-uuid"
    }
}
```

### Build Automation

```swift
// CI/CD pipeline for macOS apps
// .github/workflows/macos-ci.yml
name: macOS CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: macos-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Select Xcode version
        run: sudo xcode-select -s /Applications/Xcode_14.2.app

      - name: Install dependencies
        run: |
          brew install swiftlint
          swift package resolve

      - name: Run SwiftLint
        run: swiftlint lint --strict

      - name: Build project
        run: xcodebuild build -project MyApp.xcodeproj -scheme MyApp -configuration Debug

      - name: Run tests
        run: xcodebuild test -project MyApp.xcodeproj -scheme MyApp -configuration Debug

  release:
    needs: test
    runs-on: macos-latest
    if: github.ref == 'refs/heads/main' && github.event_name == 'push'
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Build for release
        run: |
          xcodebuild archive -project MyApp.xcodeproj -scheme MyApp -configuration Release -archivePath ./build/MyApp.xcarchive

      - name: Export archive
        run: |
          xcodebuild -exportArchive -archivePath ./build/MyApp.xcarchive -exportPath ./build -exportOptionsPlist exportOptions.plist

      # Additional steps for notarization, distribution, etc.
```

## Performance Optimization

### Memory Management

```swift
// Memory optimization techniques
class MemoryOptimizer {

    // Weak references to prevent retain cycles
    class DataLoader {
        weak var delegate: DataLoaderDelegate?

        func loadData() {
            // Simulate async loading
            DispatchQueue.global().async {
                let data = self.fetchData()
                DispatchQueue.main.async {
                    self.delegate?.dataLoader(self, didLoad: data)
                }
            }
        }

        private func fetchData() -> Data {
            // Data loading implementation
            return Data()
        }
    }

    // Unowned references for guaranteed lifetime
    class Parent {
        var child: Child?

        init() {
            self.child = Child(parent: self)
        }
    }

    class Child {
        unowned let parent: Parent

        init(parent: Parent) {
            self.parent = parent
        }
    }

    // Memory monitoring
    func logMemoryUsage() {
        var info = mach_task_basic_info()
        var count = mach_msg_type_number_t(MemoryLayout<mach_task_basic_info>.size) / 4

        let kerr = withUnsafeMutablePointer(to: &info) { infoPtr in
            infoPtr.withMemoryRebound(to: integer_t.self, capacity: 1) { intPtr in
                task_info(mach_task_self_, task_flavor_t(MACH_TASK_BASIC_INFO), intPtr, &count)
            }
        }

        if kerr == KERN_SUCCESS {
            let usedBytes = info.resident_size
            let usedMB = Double(usedBytes) / 1024.0 / 1024.0
            print("Memory usage: \(String(format: "%.2f", usedMB)) MB")
        }
    }
}

protocol DataLoaderDelegate: AnyObject {
    func dataLoader(_ loader: DataLoader, didLoad data: Data)
}
```

### CPU Optimization

```swift
// CPU performance optimization
class PerformanceOptimizer {

    // Background processing
    func performHeavyComputation(_ input: [Int]) async -> [Int] {
        await withTaskGroup(of: [Int].self) { group in
            let chunkSize = input.count / ProcessInfo.processInfo.activeProcessorCount

            for chunk in input.chunked(into: chunkSize) {
                group.addTask {
                    return self.processChunk(chunk)
                }
            }

            var results = [Int]()
            for await chunk in group {
                results.append(contentsOf: chunk)
            }
            return results.sorted()
        }
    }

    private func processChunk(_ chunk: [Int]) -> [Int] {
        return chunk.map { self.expensiveOperation($0) }
    }

    private func expensiveOperation(_ value: Int) -> Int {
        // Simulate CPU-intensive work
        var result = value
        for _ in 0..<1000 {
            result = (result * 31) % 1000000
        }
        return result
    }

    // Caching for expensive operations
    private var computationCache = [Int: Int]()

    func cachedExpensiveOperation(_ input: Int) -> Int {
        if let cached = computationCache[input] {
            return cached
        }

        let result = expensiveOperation(input)
        computationCache[input] = result
        return result
    }

    // Lazy initialization
    lazy var expensiveResource: ExpensiveResource = {
        print("Initializing expensive resource")
        return ExpensiveResource()
    }()

    // Avoid repeated string operations
    func buildLargeString(efficiently data: [String]) -> String {
        var result = ""
        result.reserveCapacity(data.reduce(0) { $0 + $1.count })
        for item in data {
            result += item
        }
        return result
    }
}

class ExpensiveResource {
    // Resource that takes time to initialize
    init() {
        // Expensive initialization
        Thread.sleep(forTimeInterval: 0.1)
    }
}

extension Array {
    func chunked(into size: Int) -> [[Element]] {
        stride(from: 0, to: count, by: size).map {
            Array(self[$0..<Swift.min($0 + size, count)])
        }
    }
}
```

## Summary

macOS development with Swift offers powerful capabilities for building professional desktop applications:

**Core Frameworks:**
- **AppKit**: Native UI components and window management
- **SwiftUI**: Declarative UI framework (macOS 10.15+)
- **Foundation**: Core functionality and data types
- **Core Data**: Object graph management and persistence

**Application Architecture:**
- Document-based or single-window applications
- MVC pattern with Cocoa bindings
- Responder chain for event handling
- Delegate pattern for customization

**Key Features:**
- Sandbox security model for user protection
- Code signing and notarization for distribution
- System integration through notifications and services
- Advanced memory management with ARC

**Development Process:**
- Xcode as primary IDE with Interface Builder
- Swift Package Manager for dependency management
- TestFlight for beta testing
- App Store Connect for distribution

**Performance Considerations:**
- Memory management optimization
- CPU-intensive task distribution
- Caching strategies
- Background processing

macOS apps can leverage the full power of desktop computing while maintaining the safety and productivity benefits of Swift development. The platform supports everything from simple utilities to complex professional applications across creative, productivity, and technical domains.
